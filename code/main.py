#!/usr/bin/env python3

from config import *
from fetch import Article
from parse import ArticleReader
from assoc_dic import AssocData
from abbr_finder import weed_out_synonyms, remove_too_long_words

def main():
    # set up things
    word = 'mountain'
    article = Article('Mount Everest', 'wiki')
    reader = ArticleReader()
    word_list = reader.get_word_list(article.content)
    association_radius = 5
    strong_threshold = None
    weak_theshold = None
    # do
    assoc_data = AssocData(association_radius, [word_list])
    potential_synonyms = assoc_data.get_potential_synonyms(word, strong_threshold, weak_theshold)
    synonyms = weed_out_synonyms(word, potential_synonyms)
    truncations = remove_too_long_words(synonyms)
    print(truncations)

if __name__ == '__main__':
    main()
