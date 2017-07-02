import pandas

class TruncationOnWordlistRunner:
    def __init__(self, wordlist_filepath, save_path):
        self.wordlist = self.open_wordlist(wordlist_filepath)
        self.save_path = save_path

    def open_wordlist(self, filepath):
        df = pandas.read_csv(filepath, names=["Word"])
        series = df["Word"]
        return series

    def run_truncator_on_wordlist(self, truncator):
        truncations_df = truncator.truncate_word_series(self.wordlist)
        return truncations_df
        
    def save_output_to_csv(self, truncations, save_path = None):
        if save_path == None:
            save_path = self.save_path
        return truncations.to_csv(save_path, index = False, header = False)

