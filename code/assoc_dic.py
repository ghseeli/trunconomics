import copy

from statistics import median,stdev


class Block:


    def __init__(self, word_list, middle_index, radius):
        start = max(0, middle_index - radius)
        end = min(len(word_list), middle_index + radius+1)
        self.before_block = word_list[start:middle_index].reverse()
        self.word = word_list[middle_index]
        self.after_block = word_list[middle_index+1:end]


class DefaultWordCleaner:


    def clean(self, word_list):
        return [self.clean_word(word) for word in word_list if isinstance(word, str)]

    def clean_word(self, word):
        return word.lower()


class AssocDic(dict):


    def __init__(self):
        self.frequency = 0
        super()

    def add_block(self, block):
        association = 10.0
        for associated_word in block:
            if associated_word not in self:
                self[associated_word] = 0.0
            self[associated_word] += association
            association = association/2.0

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


    def __init__(self, association_radius, corpus=[], cleaner=None):
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
            (before_block, word, after_block) = (block.before_block, block.word, block.after_block)
            # Feed blocks into counter
            if not self.has(word):
                self.new(word)
            for block in (before_block, after_block):
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
        self.word_to_dic[key] = AssocDic()

    def _total_get(self, key, or_else=None):
        clean_key = self.cleaner.clean_word(key)
        result = self.word_to_dic.get(clean_key, (or_else, 0))
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
            strong_associates = {associate for associate in word_dic.keys() if word_dic[associate] >= strong_threshold}
            # recurse
            for strong_associate in strong_associates:
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
        non_weak_neighbors = {n for n in neighbors if word_dic[n] > weak_threshold}
        synonyms = strong_assoc2 - non_weak_neighbors
        return synonyms
