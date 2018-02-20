from copy import deepcopy
from statistics import median, stdev

from config import default_weight_func


class Block:


    def __init__(self, word_list, middle_index, radius):
        start = max(0, middle_index - radius)
        end = min(len(word_list), middle_index + radius+1)
        self.before_wing = word_list[start:middle_index]
        self.word = word_list[middle_index]
        self.after_wing = word_list[middle_index+1:end]
        # we want to read before_wing words from *closest to farthest* distance from the middle word:
        self.before_wing.reverse()

    def tuple(self):
        """ This function makes testing easier and gives a more human friendly way to see the block. """
        return (self.before_wing, self.word, self.after_wing)

    def __str__(self):
        return str(self.tuple())


class DefaultWordCleaner:


    def clean(self, word_list):
        return [self.clean_word(word) for word in word_list if isinstance(word, str)]

    def clean_word(self, word):
        return word.lower()


class AssocDic(dict):


    def __init__(self, weight_func=default_weight_func):
        self.frequency = 0
        self.weight_func = weight_func
        super()

    def add_wing(self, wing):
        for i, associated_word in enumerate(wing):
            if associated_word not in self:
                self[associated_word] = 0.0
            distance = i + 1
            self[associated_word] += self.weight_func(distance)

    def add_block(self, block):
        self.add_wing(block.before_wing)
        self.add_wing(block.after_wing)

    def restricted(self, keys):
        """ Returns a copy of self but only with the desired keys. """
        restricted_dic = {k:v for k,v in self.items() if k in keys}
        return restricted_dic

    def get_average_score(self):
        average = 0
        num = 1
        for value in self.values():
            average = (average*num + value)/(num+1)
        return average

    def get_stdev_score(self):
        return stdev(self.values())

    def get_median_score(self):
        return median(self.values())


class AssocData:


    def __init__(self, association_radius=5, corpus=[], cleaner=None, weight_func=default_weight_func):
        # set weight function
        self.weight_func = weight_func
        # clean corpus
        if cleaner is None:
            cleaner = DefaultWordCleaner()
        self.cleaner = cleaner
        cleansed_corpus = [cleaner.clean(text) for text in corpus]
        # init radius, association dictionary
        self.radius = association_radius
        self.word_to_dic = dict()
        for word_list in cleansed_corpus:
            self._update(word_list)

    def _update(self, word_list):
        for middle_index in range(len(word_list)):
            # Find the blocks
            block = Block(word_list, middle_index, self.radius)
            word = block.word
            # Feed block into counter
            if not self.has(word):
                self.new(word)
            self[word].add_block(block)
            self[word].frequency += 1

    def has(self, key):
        """ Detect if key in dictionary """
        clean_key = self.cleaner.clean_word(key)
        return clean_key in self.word_to_dic

    def new(self, key):
        """ Add new key to dictionary """
        if self.has(key):
            raise KeyError
        self.word_to_dic[key] = AssocDic(weight_func=self.weight_func)

    def _total_get(self, key, or_else=None):
        clean_key = self.cleaner.clean_word(key)
        result = self.word_to_dic.get(clean_key, or_else)
        return result

    def get(self, key, or_else=None):
        return self._total_get(key, or_else)

    def __getitem__(self, key):
        result = self.get(key)
        if result is None:
            raise KeyError(key)
        return result

    def get_normalized_dict(self, key):
        unnormalized_dict = self[key]
        freq = unnormalized_dict.frequency
        return {k:(unnormalized_dict[k]/freq) for k in unnormalized_dict}

    def get_strong_associates(self, word, distance, strong_threshold=None):
        """ Returns a SET of strong associates equal to distance or CLOSER than given distance. """
        if distance < 0:
            raise ValueError
        if distance == 0:
            strong_associates = {word}
        else:
            word_dic = self[word]
            if strong_threshold is None:
                strong_threshold = word_dic.get_average_score() + word_dic.get_stdev_score()
            strong_associates = {a for a in word_dic.keys() if word_dic[a] >= strong_threshold}
            # recurse
            for strong_associate in deepcopy(strong_associates):
                next_level_strong_associates = self.get_strong_associates(strong_associate, distance - 1, strong_threshold)
                strong_associates.update(next_level_strong_associates)
        return strong_associates

    def get_potential_synonyms(self, word, strong_threshold=None, weak_threshold=None):
        # NORMALIZATION HAPPENS HERE.  but i feel i can get easily confused, because get_strong_associates needs to be given a normalized threshold.  and how to remember that?
        # normalize the thresholds
        # word_list = sanitize_word_list(word_list)
        # number_of_times_word_appears = word_list.count(word)
        # strong_threshold = strong_threshold * number_of_times_word_appears
        # weak_threshold = weak_threshold * number_of_times_word_appears
        # print("THRESH")
        # print(strong_threshold)
        # print(weak_threshold)
        strong_assoc2 = self.get_strong_associates(word, 2, strong_threshold)
        word_dic = self[word]
        if weak_threshold is None:
            weak_threshold = word_dic.get_average_score() - 0.01 * word_dic.get_stdev_score()
        neighbors = set(word_dic.keys())
        non_weak_neighbors = {n for n in neighbors if word_dic[n] >= weak_threshold}
        synonyms = strong_assoc2 - non_weak_neighbors
        return synonyms
