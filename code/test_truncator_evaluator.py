import pytest

from truncator_evaluator import *

def test_init():
	TruncatorEvaluator()

def test_test_file():
	tt = TruncatorTester()
	tt.test_file('../data/basic_test_file.csv')
