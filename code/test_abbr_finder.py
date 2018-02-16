import json
from os import path
import sys
THIS_DIR = path.dirname(path.abspath(__file__))
PYTHON_DIR = path.dirname(THIS_DIR)
sys.path.insert(0, PYTHON_DIR)

import pytest
import mediawikiapi as wiki

from abbr_finder import *
from assoc_dic import AssocDic
from parse import ArticleReader

def test_weed_out_synonyms():
    word = "characteristic"
    potential_synonyms = {'characteristic', 'field', 'char', 'is', 'p', 'bla', 'a'}
    synonyms = weed_out_synonyms(word, potential_synonyms)
    assert synonyms == {'characteristic', 'char', 'is', 'a'}
