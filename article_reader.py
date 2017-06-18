""" A simple content parser that we can use on our articles.

The pyparsing module has many features, and a helpful starting point is
http://pyparsing.wikispaces.com/HowToUsePyparsing

as well as looking at examples at
http://pyparsing.wikispaces.com/Examples
"""
from pyparsing import Word, CharsNotIn, Group, Optional, Suppress, ZeroOrMore

# these variables will be used to define valid lists of characters
lowers = 'qwertyuiopasdfghjklzxcvbnm'
uppers = lowers.upper()
word_symbols = '-_'
digits = '1234567890'
word_chars = lowers + uppers + word_symbols + digits

# define grammar
word = Word(word_chars)
delim = CharsNotIn(word_chars)
delim_and_word = Group(Suppress(Optional(delim)) + word)
content = ZeroOrMore(delim_and_word)

# try parsing
string = 'Conditional and unconditional convergence. Operator Theory: Advances and Applications. 94. Translated by Andrei Iacob from the Russian-language. Basel: Birkhäuser Verlag. pp. viii+156. ISBN 3-7643-5401-1. MR 1442255. \nWeisstein, Eric (2005). Riemann Series Theorem. Retrieved May 16, 2005.'
parsed_data = content.parseString(string)
word_list = [group[0] for group in parsed_data]
print(word_list)
