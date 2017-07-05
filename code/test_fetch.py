import pytest

from fetch import *

def test_fetch_arxiv_article():
    name = '9711102'
    content = fetch_arxiv_article(name)

