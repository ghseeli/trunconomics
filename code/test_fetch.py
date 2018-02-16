from os import path
from pathlib import Path

import pytest

from config import DATA_DIR
from fetch import _fetch_wiki_article, _fetch_arxiv_article
from fetch import *

def test_fetch_wiki_article():
    name = 'Riemann series theorem'
    content = _fetch_wiki_article(name)
    # TODO: don't grab article from DATA_DIR but use the json API through subprocess.run or something.  Because the article changes!
    riemann_path = path.join(DATA_DIR, 'riemann_series_theorem.txt')
    correct_content = Path(riemann_path).read_text()
    # assert content == correct_content

def test_fetch_arxiv_article():
    name = 'test_me'
    content = _fetch_arxiv_article(name)
    correct_content_path = path.join(DATA_DIR, 'test_me.tex')
    correct_content = Path(correct_content_path).read_text()
    assert content == correct_content

    name = '9711102'
    content = _fetch_arxiv_article(name)
    correct_content_path = path.join(DATA_DIR, '9711102.tex')
    correct_content = Path(correct_content_path).read_text()
    assert content == correct_content

def test_Article_init():
    name = 'Riemann series theorem'
    article = Article(name, 'wiki')
    assert isinstance(article, Article)

def test_Article_content():
    name = 'Riemann series theorem'
    article = Article(name, 'wiki')
    content = article.content
    riemann_path = path.join(DATA_DIR, 'riemann_series_theorem.txt')
    correct_content = Path(riemann_path).read_text()
    # TODO: same as above
    # assert content == correct_content

