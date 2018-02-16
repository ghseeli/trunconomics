#!/usr/bin/env python3
import pandas

from config import *
from fetch import Article
from parse import ArticleReader
from assoc_dic import AssocData
from abbr_finder import weed_out_synonyms, remove_too_long_words

def find_truncations(word, article_name, archive):
    # set up things
    article = Article(article_name, archive)
    reader = ArticleReader()
    word_list = reader.get_word_list(article.content)
    association_radius = 5
    strong_threshold = None
    weak_theshold = None
    # do
    assoc_data = AssocData(association_radius, [word_list])
    potential_synonyms = assoc_data.get_potential_synonyms(word, strong_threshold, weak_theshold)
    synonyms = weed_out_synonyms(word, potential_synonyms)
    truncations = remove_too_long_words(word, synonyms)
    return truncations

def main(**kwargs):
    """ This function is overloaded.  The arguments determine how we handle the input data.
    """
    if 'command' not in kwargs.keys():
        raise ValueError
    command = kwargs['command']
    if command == 'single article':
        truncs = find_truncations(kwargs['word'], kwargs['article'], kwargs['archive'])
        print(truncs)
    if command == 'multi article':
        df = pandas.read_csv(kwargs['csv_path'], names=['word', 'article', 'archive'])
        for _, row in df.iterrows():
            print('{}:'.format(row[0]))
            main(command='single article', word=row[0], article=row[1], archive=row[2])

if __name__ == '__main__':
    # main(command='single article', word='mountain', article='Mount Everest', archive='wiki')
    main(command='multi article', csv_path=path.join(DATA_DIR, 'word_and_wiki.csv'))

