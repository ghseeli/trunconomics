import pytest

import test_fixtures
from assoc_dic import *

def test_empty_initialization():
    assoc_dic = AssocDic(1,[])
    assert assoc_dic is not None

def test_basic_make_assoc_dic():
    assoc_dic = test_fixtures.dic_gen.get_dict()
    assert len(assoc_dic.assoc_dic) != 0

def test_get_function():
    assoc_dic = test_fixtures.dic_gen.get_dict()
    pos_result = assoc_dic.get('fox')
    assert 'red' in pos_result
    neg_result = assoc_dic.get('asdfgh', 5)
    assert neg_result == 5

    
