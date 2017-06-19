""" These functions take in a list of words (from a corpus), and tries to identify abbreviations by looking at which words appear close to each other.
"""
import copy
import Levenshtein as lev

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

def is_non_word(word, dictionary):
	return word in dictionary.keys()

def get_strong_associates(assoc_dic, word, distance, strong_threshold):
	""" Returns a SET of strong associates equal to distance or CLOSER than given distance. """
	if distance < 0:
		raise ValueError
	if distance == 0:
		strong_associates = {word}
	else:
		word_dic = assoc_dic[word]
		print(word_dic)
		strong_associates = {associate for associate in word_dic.keys() if word_dic[associate] >= strong_threshold}
		print(strong_associates)
		strong_associates_copy = copy.deepcopy(strong_associates)
		for strong_associate in strong_associates_copy:
			strong_associates.update(get_strong_associates(assoc_dic, strong_associate, distance - 1, strong_threshold))
	return strong_associates

def get_potential_synonyms(assoc_dic, word, strong_threshold, weak_threshold):
	strong_assoc2 = get_strong_associates(assoc_dic, word, 2, strong_threshold)
	word_dic = assoc_dic[word]
	neighbors = set(word_dic.keys())
	non_weak_neighbors = {neighbor for neighbor in neighbors if word_dic[neighbor] > weak_threshold}
	synonyms = strong_assoc2 - non_weak_neighbors
	return synonyms

def weed_out_synonyms(word, potential_synonyms):
	""" Takes in a word and a list of 'supposed' synonyms, and deletes the ones whose Levenshtein distance is too high. """
	real_synonyms = set()
	for synonym in potential_synonyms:
		max_distance = abs(len(word) - len(synonym))
		abbr_len = min(len(word), len(synonym))
		forgiveness = 1 + 1/7 * abbr_len
		if lev.distance(word, synonym) <= max_distance + forgiveness:
			# Then it's a synonym!
			real_synonyms.add(synonym)
	return real_synonyms

# Below are three little tests, which should really be in a separate file:
word_list = ['Conditional', 'and', 'unconditional', 'convergence', 'Operator', 'Theory', 'Advances', 'Basel', 'and', 'Applications', '94', 'Translated', 'by', 'Andrei', 'Iacob', 'from', 'the', 'and', 'Russian-language', 'Basel', 'Birkh', 'user', 'Verlag', 'pp', 'viii', '156', 'ISBN', '3-7643-5401-1', 'MR', '1442255', 'Weisstein', 'Eric', '2005', 'Riemann', 'Series', 'Theorem', 'Retrieved', 'May', '16', '2005']
assoc_dic = make_assoc_dic(word_list, 2)
print(assoc_dic['and'])

sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
word_list = sentence.split()
assoc_dic = make_assoc_dic(word_list, 2)
strong_assoc = get_strong_associates(assoc_dic, "characteristic", 2, 9.0)
print(strong_assoc)

sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
word_list = sentence.split()
assoc_dic = make_assoc_dic(word_list, 2)
synonyms = get_potential_synonyms(assoc_dic, "characteristic", 9.0, 1.0)
print(synonyms)
print()

word = "characteristic"
sentence = 'bla bla the characteristic of a field is p  The char of a field is p'
word_list = sentence.split()
assoc_dic = make_assoc_dic(word_list, 2)
potential_synonyms = get_potential_synonyms(assoc_dic, word, 9.0, 1.0)
synonyms = weed_out_synonyms(word, potential_synonyms)
print(synonyms)
