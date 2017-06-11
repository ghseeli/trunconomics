import pandas

class TruncatorTester:
    def test_file(self, result_csv_filepath):
        raw_data = pandas.read_csv(result_csv_filepath, names = ["Word", "Truncation"])
        return self.test_data_frame(raw_data)

    def test_data_frame(self, df):
        truncation_collisions = self.summarize_truncation_collisions(df)
        raw_character_differences = self.count_raw_character_difference(df)
        total_character_saves = raw_character_differences["raw_character_difference"].sum()
        number_test_words = self.count_total_words(df)
        return {"total_collisions": truncation_collisions,
                "total_character_saves": total_character_saves,
                "total_words_evaluated": number_test_words}

    def count_truncation_collisions(self, df): 
        duplicate_counts = df.groupby(["Truncation"]).size()       
        return duplicate_counts

    def summarize_truncation_collisions(self, df):
        duplicate_counts = self.count_truncation_collisions(df)
#        drop_non_collisions =
        adjusted_duplicate_counts = duplicate_counts-1
        total_collisions = adjusted_duplicate_counts.sum()
        return total_collisions
    
    def count_raw_character_difference(self, df):
        def raw_character_difference(word1, word2):
            return len(word1)-len(word2)        
        df["raw_character_difference"] = list(map(raw_character_difference, df["Word"], df["Truncation"]))
        return df

    def count_total_words(self,df):
        return df["Word"].count()

