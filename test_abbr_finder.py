import pytest
from abbr_finder import *

import mediawikiapi as wiki
from article_reader import ArticleReader

def test_make_assoc_dic():
	word_list = ['Conditional', 'and', 'unconditional', 'convergence', 'Operator', 'Theory', 'Advances', 'Basel', 'and', 'Applications', '94', 'Translated', 'by', 'Andrei', 'Iacob', 'from', 'the', 'and', 'Russian-language', 'Basel', 'Birkh', 'user', 'Verlag', 'pp', 'viii', '156', 'ISBN', '3-7643-5401-1', 'MR', '1442255', 'Weisstein', 'Eric', '2005', 'Riemann', 'Series', 'Theorem', 'Retrieved', 'May', '16', '2005']
	assoc_dic = make_assoc_dic(word_list, 2)
	print(assoc_dic['and'])

def test_get_strong_associates():
	sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
	word_list = sentence.split()
	assoc_dic = make_assoc_dic(word_list, 2)
	strong_assoc = get_strong_associates(assoc_dic, "characteristic", 2, 9.0)
	print(strong_assoc)

def test_get_potential_synonyms():
	sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
	word_list = sentence.split()
	assoc_dic = make_assoc_dic(word_list, 2)
	potential_synonyms = get_potential_synonyms(word_list, assoc_dic, "characteristic", 9.0, 1.0)
	assert potential_synonyms == {'characteristic', 'field', 'char'}


def test_weed_out_synonyms():
	word = "characteristic"
	sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
	word_list = sentence.split()
	assoc_dic = make_assoc_dic(word_list, 2)
	potential_synonyms = get_potential_synonyms(word_list, assoc_dic, word, 9.0, 1.0)
	synonyms = weed_out_synonyms(word, potential_synonyms)
	assert synonyms == {'characteristic', 'char'}

# okay, large_data_set isn't really a method, and pytest doesn't follow this convention
def test_large_data_set():
	# set up things
	word = "series"
	article_name = "Riemann series theorem"
	page = wiki.page(article_name)
	content = page.content
	reader = ArticleReader()
	word_list = reader.get_word_list(content)
	association_radius = 5
	strong_threshold = 9.0
	weak_theshold = 1.0
	# do
	assoc_dic = make_assoc_dic(word_list, association_radius)
	potential_synonyms = get_potential_synonyms(word_list, assoc_dic, word, strong_threshold, weak_theshold)
	synonyms = weed_out_synonyms(word, potential_synonyms)
	print(synonyms)
