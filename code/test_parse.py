from os import path
from pathlib import Path

import pytest

from parse import *
from config import DATA_DIR

def test_ArticleReader_init():
    ArticleReader()

def test_ArticleReader_get_word_list():
    # try parsing
    string = 'Conditional and unconditional convergence. Operator Theory: Advances and Applications. 94. Translated by Andrei Iacob from the Russian-language. Basel: Birkhäuser Verlag. pp. viii+156. ISBN 3-7643-5401-1. MR 1442255. \nWeisstein, Eric (2005). Riemann Series Theorem. Retrieved May 16, 2005.'
    reader = ArticleReader()
    word_list = reader.get_word_list(string)
    print(word_list)
