import pytest

import test_fixtures
from assoc_dic import *


# Block
def test_make_block():
    # standard block
    word_list = ['The','quick','red','fox','jumped','over','the','brown','dog']
    b = Block(word_list,3,2)
    assert b.tuple() == (['red', 'quick'],'fox',['jumped','over'])

    # left end block
    word_list = ['The','quick','red','fox','jumped','over','the','brown','dog']
    b = Block(word_list,0,2)
    assert b.tuple() == ([],'The',['quick','red'])

    # right end block
    word_list = ['The','quick','red','fox','jumped','over','the','brown','dog']
    b = Block(word_list,len(word_list)-1,2)
    assert b.tuple() == (['brown', 'the'],'dog',[])

    # degenerate block
    word_list = ['The','quick','red','fox','jumped','over','the','brown','dog']
    b = Block(word_list,3,0)
    assert b.tuple() == ([],'fox',[])


# AssocData
def test_make_assoc_data():
    # basic init
    AssocData()

    # with a word list
    word_list = ['Conditional', 'and', 'unconditional', 'convergence', 'Operator', 'Theory', 'Advances', 'Basel', 'and', 'Applications', '94', 'Translated', 'by', 'Andrei', 'Iacob', 'from', 'the', 'and', 'Russian-language', 'Basel', 'Birkh', 'user', 'Verlag', 'pp', 'viii', '156', 'ISBN', '3-7643-5401-1', 'MR', '1442255', 'Weisstein', 'Eric', '2005', 'Riemann', 'Series', 'Theorem', 'Retrieved', 'May', '16', '2005']
    assoc_data = AssocData(2, [word_list])

def test_get_function():
    assoc_data = test_fixtures.dic_gen.get_dict()
    pos_result = assoc_data.get('fox')
    assert 'red' in pos_result

    neg_result = assoc_data.get('asdfgh', 5)
    assert neg_result == 5

def test_getitem_function():
    assoc_data = test_fixtures.dic_gen.get_dict()
    pos_result = assoc_data['fox']
    assert 'red' in pos_result

def test_frequency():
    assoc_data = test_fixtures.dic_gen.get_dict()
    pos_result = assoc_data['fox'].frequency
    assert pos_result == 1
    pos_result2 = assoc_data['the'].frequency
    assert pos_result2 == 2

def test_get_strong_associates():
    sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
    word_list = sentence.split()
    ad = AssocData(2, [word_list])
    strong_assoc = ad.get_strong_associates("characteristic", 1, 9.0)
    assert strong_assoc == {'the', 'of'}

    strong_assoc = ad.get_strong_associates("characteristic", 1, 2.0)
    assert strong_assoc == {'the', 'of', 'bla', 'a'}

    strong_assoc = ad.get_strong_associates("characteristic", 2, 9.0)
    assert strong_assoc == {'the','of', 'bla', 'characteristic', 'a', 'p', 'char', 'field'}

def test_get_potential_synonyms():
    sentence = 'bla bla the characteristic of a field is p  the char of a field is p'
    word_list = sentence.split()
    ad = AssocData(2, [word_list])
    # print(json.dumps(assoc_data.assoc_data, indent=4))
    potential_synonyms = ad.get_potential_synonyms("characteristic", 2.0, 9.0)
    assert potential_synonyms == {'characteristic', 'field', 'char', 'is', 'p', 'bla', 'a'}

