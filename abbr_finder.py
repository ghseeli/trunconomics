""" These functions take in a list of words (from a corpus), and tries to identify abbreviations by looking at which words appear close to each other.
"""
import copy

def make_assoc_dic(word_list, association_radius):
	""" Make an association dictionary """

	# Set up variables
	assoc_dic = dict()
	word_seq = copy.deepcopy(word_list)
	block_length = 2 * association_radius + 1

	# Actually do things
	for i in range(len(word_list) - block_length):
		# Find the blocks
		before_block = word_seq[i : i + association_radius]
		word = word_seq[i + association_radius]
		after_block = word_seq[i + association_radius + 1 : i + block_length]
		# Reverse the before_block
		before_block.reverse()
		# Feed blocks into counter
		if word not in assoc_dic:
			assoc_dic[word] = dict()
		for block in (before_block, after_block):
			assoc_dic[word] = add_block_to_dic(assoc_dic[word], block)
	return assoc_dic

def add_block_to_dic(word_dic, block):
	association = 10.0
	for associated_word in block:
		if associated_word not in word_dic:
			word_dic[associated_word] = 0.0
		word_dic[associated_word] += association
		association = association/2.0
	return word_dic

word_list = ['Conditional', 'and', 'unconditional', 'convergence', 'Operator', 'Theory', 'Advances', 'Basel', 'and', 'Applications', '94', 'Translated', 'by', 'Andrei', 'Iacob', 'from', 'the', 'and', 'Russian-language', 'Basel', 'Birkh', 'user', 'Verlag', 'pp', 'viii', '156', 'ISBN', '3-7643-5401-1', 'MR', '1442255', 'Weisstein', 'Eric', '2005', 'Riemann', 'Series', 'Theorem', 'Retrieved', 'May', '16', '2005']
assoc_dic = make_assoc_dic(word_list, 2)
print(assoc_dic['and'])
