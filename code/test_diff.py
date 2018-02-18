import pytest

from config import *
from diff import *

def test_diff():
	# identical files
	p1 = path.join(IN_DIR, 'diff1.txt')
	out = diff(p1, p1)
	assert out == ''

	# different files
	p1 = path.join(IN_DIR, 'diff1.txt')
	p2 = path.join(IN_DIR, 'diff2.txt')
	out = diff(p1, p2)
	assert out != ''

def test_is_different():
	# identical files
	p1 = path.join(IN_DIR, 'diff1.txt')
	exist, are_different = is_different(p1, p1)
	assert (exist, are_different) == (True, False)

	# file that doesn't exist
	p1 = path.join(IN_DIR, 'thisfiledoesntexist')
	exist, are_different = is_different(p1, p1)
	assert (exist, are_different) == (False, None)
