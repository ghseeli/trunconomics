import pytest
from truncator_testor import *

def test_init():
	TruncatorTester()

def test_test_file():
	tt = TruncatorTester()
	tt.test_file('data/basic_test_file.csv')
