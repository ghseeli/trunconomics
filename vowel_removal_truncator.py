import pandas

class VowelRemovalTruncator:
    def __init__(self):
        self.vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
    def truncate_word_series(self, word_series):
        truncations = pandas.Series([self.truncate_word(word) for word in word_series])
        d = {'Word' : word_series, "Truncation" : truncations}
        return pandas.DataFrame(d, columns=['Word','Truncation'])

    def truncate_word(self, word):
        word = str(word)
        if len(word) > 2:
            first_letter = word[0]
            last_letter = word[-1]
            middle = word[1:-1]
            return first_letter + ''.join([l for l in middle if l not in self.vowels]) + last_letter
        else:
            return word
