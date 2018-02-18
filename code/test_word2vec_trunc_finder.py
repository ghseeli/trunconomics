import pytest

from config import *
from word2vec_trunc_finder import *


def test_init():
	in_path = path.join(IN_DIR, 'text8')
	Word2VecTruncFinder(in_path)

def test_get_synonyms():
	in_path = path.join(IN_DIR, 'text8')
	tf = Word2VecTruncFinder(in_path)
	syn = tf.get_synonyms('dog', 2)
	assert syn == ['cat', 'goat']

def test_get_truncations():
	# no truncations
	in_path = path.join(IN_DIR, 'text8')
	tf = Word2VecTruncFinder(in_path)
	truncs = tf.get_truncations('dog', 2)
	assert truncs == []

	# one truncation
	in_path = path.join(IN_DIR, 'text8')
	tf = Word2VecTruncFinder(in_path)
	truncs = tf.get_truncations('princess', 5)
	assert truncs == ['duchess', 'prince', 'consort', 'anne']

