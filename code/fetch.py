# This creates a general content fetcher.
import subprocess

import mediawikiapi as wiki
from pathlib import Path


def fetch_wiki_article(name):
    """ This shows how to fetch wikipedia articles: https://pypi.python.org/pypi/mediawikiapi/1.0
The documentation is here: https://github.com/lehinevych/MediaWikiAPI/tree/master/docs/source (or actually, you should build it with sphinx if you really want to see it correctly)
"""
    article = wiki.page(article_name)
    content = article.content
    return content

def fetch_arxiv_article(name):
    """ Fetch article from guava server """
    """ Maybe we can set up a static file server for articles  on guava, and then just request them?  With wget? """
    command = ['curl', 'learnnation.org/articles/{}.tex'.format(name)]
    content = subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return content


class Article:


    def __init__(self, name, archive):
        """ name -- the name of the article you want
        archive -- the archive you want the article from (wiki, arXiv)
        """
        archive = archive.lower().trim()
        if archive in {'wiki', 'wikipedia'}:
            self.content = fetch_wiki_article(name)
        elif archive == 'arxiv':
            self.content = fetch_arxiv_article(name)
        else:
            raise ValueError('Archive not recognized.')


