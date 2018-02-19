""" This file contains configuration settings for the entire project.
"""
from os import path

# Useful paths
BASE_DIR = path.dirname(path.abspath(__file__))
CODE_DIR = path.join(BASE_DIR, 'code')
DATA_DIR = path.join(BASE_DIR, 'data')
IN_DIR = path.join(BASE_DIR, 'test_inputs')
OUT_DIR = path.join(BASE_DIR, 'test_outputs')
