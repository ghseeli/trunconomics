from os import path
from pathlib import Path

import pytest

from fetch import *
from config import DATA_DIR

def test_fetch_wiki_article():
    name = 'Riemann series theorem'
    content = fetch_wiki_article(name)
    riemann_path = path.join(DATA_DIR, 'riemann_series_theorem.txt')
    correct_content = Path(riemann_path).read_text()
    assert content == correct_content

def test_fetch_arxiv_article():
    name = 'test_me'
    content = fetch_arxiv_article(name)
    correct_content_path = path.join(DATA_DIR, 'test_me.tex')
    correct_content = Path(correct_content_path).read_text()
    assert content == correct_content

    name = '9711102'
    content = fetch_arxiv_article(name)
    correct_content_path = path.join(DATA_DIR, '9711102.tex')
    correct_content = Path(correct_content_path).read_text()
    assert content == correct_content
