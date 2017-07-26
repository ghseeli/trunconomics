""" This creates a general content fetcher. """
import subprocess

import mediawikiapi as wiki
from pathlib import Path


def fetch_wiki_article(name):
    """ This shows how to fetch wikipedia articles: https://pypi.python.org/pypi/mediawikiapi/1.0
The documentation is here: https://github.com/lehinevych/MediaWikiAPI/tree/master/docs/source (or actually, you should build it with sphinx if you really want to see it correctly)
"""
    page = wiki.page(name)
    content = page.content
    return content

def fetch_arxiv_article(name):
    """ Fetch article from guava server """
    url = 'learnnation.org/articles/{}.tex'.format(name)
    command = ['curl', url]
    completed_process = subprocess.run(command, check=True, stdout=subprocess.PIPE)
    # convert bytes object to str object with .decode()
    content = completed_process.stdout.decode()
    return content


class Article:


    def __init__(self, name, archive):
        """ name -- the name of the article you want
        archive -- the archive you want the article from (wiki, arXiv)
        """
        archive = archive.lower().strip()
        if archive in {'wiki', 'wikipedia'}:
            self.content = fetch_wiki_article(name)
        elif archive == 'arxiv':
            self.content = fetch_arxiv_article(name)
        else:
            raise ValueError('Archive not recognized.')


