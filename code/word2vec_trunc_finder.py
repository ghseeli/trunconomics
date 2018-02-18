""" Use the existing word2vec library to find truncations for words """
import os
import shutil

import word2vec as w2v

from config import *
from diff import is_different


def weed(word, trunc_candidates):
	""" Well we should probably just use the WEED OUT SYNONYMS function from abbr_finder.py instead """
	truncs = []
	for trunc_cand in trunc_candidates:
		if len(trunc_cand) < len(word):
			truncs.append(trunc_cand)
	return truncs


class Word2VecTruncFinder:
	""" When given a word, this finder will simply find 'synonyms' for the word by finding vectors nearby.  It will then perform a filter on those synonyms to see which ones qualify as 'truncations'. """
	def __init__(self, text_data_path):
		""" see http://nbviewer.jupyter.org/github/danielfrg/word2vec/blob/master/examples/word2vec.ipynb for example """
		cache_path = text_data_path + '.cache'
		self.vec_data_path = text_data_path + '-vecs.bin'
		# Don't unnecessarily create the vectors again
		exist, are_different = is_different(text_data_path, cache_path)
		if os.path.exists(self.vec_data_path) and exist and not are_different:
			pass
		else:
			# create vectors
			w2v.word2vec(
				text_data_path,
				self.vec_data_path,
				size=100,
				verbose=True)
			shutil.copy(text_data_path, cache_path)
		# vs is the 'model' or 'vector space'
		self.vs = w2v.load(self.vec_data_path)

	def get_synonyms(self, word, num=5):
		""" Get the 'num' closest words to word in the vector space. """
		sim_word_indexes, sim_word_metrics = self.vs.cosine(word)
		# the following are ordered by best match
		sim_words = self.vs.vocab[sim_word_indexes]
		# best_matches = self.vs.generate_response(sim_word_indexes, sim_word_metrics).tolist()[:num]
		return sim_words[:num].tolist()

	def get_truncations(self, word, num=2):
		syns = self.get_synonyms(word, num)
		truncs = weed(word, syns)
		return truncs

