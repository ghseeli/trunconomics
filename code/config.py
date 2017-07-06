""" This file contains configuration settings for things in the code directory.  It inherits configuration things from conf.py in the root of the repo.
"""
from os import path
import sys

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from conf import CODE_DIR, DATA_DIR
