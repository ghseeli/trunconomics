#!/usr/bin/env python3
import pandas

from config import *
import fetch
from abbr_finder import weed_out_synonyms, remove_too_long_words
from truncators import vowel_removal_truncator, assoc_dic, word2vec_trunc_finder
from truncator_evaluator import TruncatorEvaluator


def get_truncator(name):
    name_to_trunc_class = {
        'dist2syns': assoc_dic.Truncator,
        'vowelremover': vowel_removal_truncator.VowelRemovalTruncator,
        'word2vec': word2vec_trunc_finder.Word2VecTruncFinder,
    }
    truncator = name_to_trunc_class[name]
    return truncator

def evaluate_truncations(**kwargs):
    # init inputs
    data = kwargs['data']
    word = kwargs['word']
    method = kwargs['method']
    # setup truncator
    trunc_input_data = fetch.fetch(method, data)
    Truncator = get_truncator(truncator_name)
    t = Truncator(trunc_input_data)
    # get truncations
    truncations = t.get_truncations(word)
    # get other stats
    evaluator = TruncatorEvaluator()
    # run the following line if you want to.  commented out just bc its slow
    # out = evaluator.test_file(
    #     path.join(OUT_DIR, "out.csv"),
    #     "../fonts/Monaco.dfont"
    # )
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
    elif command == 'multi article':
        df = pandas.read_csv(kwargs['csv_path'], names=['word', 'article', 'archive'])
        for _, row in df.iterrows():
            print('{}:'.format(row[0]))
            main(command='single article', word=row[0], article=row[1], archive=row[2])
    elif command == 'evaluate truncs':
        out = evaluate_truncations(**kwargs)
        print(out)

if __name__ == '__main__':
    # main(command='multi article', csv_path=path.join(DATA_DIR, 'word_and_wiki.csv'))
    # main(command='single article', word='mister', article='Mr.', archive='wiki')
    # main(command='evaluate truncs')
    main(
        command='evaluate truncs',
        data={
            method='wiki',
            title='Mount Everest',
        },
        word='mountain',
        method='word2vec')
