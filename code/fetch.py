""" This creates a general content fetcher. """
import subprocess

import mediawikiapi as wiki

from parse import CorpusReader


def _fetch_wiki_article(name):
    """ This shows how to fetch wikipedia articles: https://pypi.python.org/pypi/mediawikiapi/1.0

    The documentation is here: https://github.com/lehinevych/MediaWikiAPI/tree/master/docs/source (or actually, you should build it with sphinx if you really want to see it correctly)
    """
    page = wiki.page(name)
    content = page.content
    reader = CorpusReader()
    wordlist = reader.get_wordlist(content)
    return wordlist

def _fetch_arxiv_article(name):
    """ Fetch article from guava server """
    url = 'learnnation.org/articles/{}.tex'.format(name)
    command = ['curl', url]
    completed_process = subprocess.run(command, check=True, stdout=subprocess.PIPE)
    # convert bytes object to str object with .decode()
    content = completed_process.stdout.decode()
    reader = CorpusReader()
    wordlist = reader.get_wordlist(content)
    return wordlist

def _fetch_wordlist_vertical_csv(filepath):
    df = pandas.read_csv(filepath, names=["Word"])
    series = df["Word"]
    return list(series)

def _fetch_textfile(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
    reader = CorpusReader()
    wordlist = reader.get_wordlist(content)
    return wordlist


class _Corpus:
    """ A 'corpus' is written text.  The words have an *order*, and they can occur more than once. """


    def __init__(self, method, **kwargs):
        """
        method -- the method to follow for information retrieval
        name -- the name of the article you want
        archive -- the archive you want the article from (wiki, arXiv)
        """
        if method == 'wiki':
            title = kwargs['title']
            self.wordlist = _fetch_wiki_article(title)
        elif method == 'arxiv':
            title = kwargs['title']
            self.wordlist = _fetch_arxiv_article(title)
        elif method == 'textfile':
            filepath = kwargs['filepath']
            self.wordlist = _fetch_textfile(filepath)
        else:
            raise ValueError('method not recognized')



class _Vocabulary:
    """ A 'vocabulary' is merely a set of words. """


    def __init__(self, method, **kwargs):
        """
        method -- the method to follow for information retrieval
        """
        if method == 'vertical-csv':
            filepath = kwargs['filepath']
            wordlist = _fetch_wordlist_vertical_csv(filepath)
            # remove possible repetition
            self.words = list(set(wordlist))
        elif method == 'horizontal-csv':
            # for a list of words separated by commas
            raise Exception('not yet programmed.')
        elif method == 'corpus':
            corpus = kwargs['corpus']
            content = corpus.content
            self.words = list(set(content))
        else:
            raise ValueError('method not recognized')



def fetch(method, dic):
    if method in ['vertical-csv', 'horizontal-csv']:
        out = _Vocabulary(method, **dic)
    elif method in ['textfile', 'arxiv', 'wiki']:
        out = _Corpus(method, **dic)
    else:
        raise ValueError('method not recognized')
    return out

