import copy

class Block:
    def __init__(self, word_list, middle_index, radius):
        start = max(0, middle_index - radius)
        end = min(len(word_list), middle_index + radius+1)
        self.before_block = word_list[start:middle_index]
        self.word = word_list[middle_index]
        self.after_block = word_list[middle_index+1:end]

class NoLowerCaseWordCleaner:
    def clean(self, list_of_words):
        return [self.clean_word(word) for word in list_of_words]
    
    def clean_word(self, word):
        return word.lower()
        

class AssocDic:
    def __init__(self, association_radius, corpus=[], cleaner=None):
        if cleaner is None:
            cleaner = NoLowerCaseWordCleaner()
        self.cleaner = cleaner
        cleansed_corpus = [cleaner.clean(text) for text in corpus]
        self.assoc_dic = dict()
        for word_list in cleansed_corpus:
            block_length = 2 * association_radius + 1

            # Actually do things
            for middle_index in range(len(word_list)):
                # Find the blocks
                block = Block(word_list, middle_index, association_radius)
                (before_block, word, after_block) = (block.before_block, block.word, block.after_block)
                # Reverse the before_block
                before_block.reverse()
                # Feed blocks into counter
                if word not in self.assoc_dic:
                    self.assoc_dic[word] = dict()
                for block in (before_block, after_block):
                    self.assoc_dic[word] = self.add_block_to_dic(self.assoc_dic[word], block)

    def add_block_to_dic(self, word_dic, block):
        association = 10.0
        for associated_word in block:
            if associated_word not in word_dic:
                word_dic[associated_word] = 0.0
            word_dic[associated_word] += association
            association = association/2.0
        return word_dic

    def get(self, key, or_else = None):
        clean_key = self.cleaner.clean_word(key)
        return self.assoc_dic.get(clean_key, or_else)

    def __getitem__(self, key):
        result = self.get(key)
        if result is None:
            raise KeyError(key)
        return result

    def is_non_word(self, word):
        return word in self.assoc_dic
