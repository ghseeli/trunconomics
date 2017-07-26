#!/bin/zsh
# This install script is specific to Mac OSX.
# Besides being an install script, this is useful as a (hopefully) exhaustive list of dependencies.

# Install Levenshtein (but import as 'Levenshtein' in python)
pip3 install python-Levenshtein

# Install pyparsing
## Install bs4, even if just to get a pointer to BeautifulSoup that you already have
pip3 install bs4
pip3 install pyparsing

# Install pygame
## Install SDL, but only if you don't have the file SDL.h.
brew install sdl
pip3 install pygame

# Install pandas
pip3 install pandas

# Install pytest (but use command 'py.test' in terminal)
pip3 install pytest

# Install mediawikiapi (MediaWikiAPI is compatible only with Python 3.3+)
pip3 install mediawikiapi
