""" A simple content parser that we can use on our articles.

The pyparsing module has many features, and a helpful starting point is
http://pyparsing.wikispaces.com/HowToUsePyparsing

as well as looking at examples at
http://pyparsing.wikispaces.com/Examples
"""
from pyparsing import Word, CharsNotIn, Group, Optional, Suppress, ZeroOrMore


# This was originally designed for wikipedia articles.  But now we probably want to subclass in order to read different types of articles.
class CorpusReader:


    def __init__(self):
        self.init_parser()

    def init_parser(self):
        # these variables will be used to define valid lists of characters
        lowers = 'qwertyuiopasdfghjklzxcvbnm'
        uppers = lowers.upper()
        alphas = lowers + uppers
        word_symbols = '-_'
        digits = '1234567890'
        word_chars = alphas + word_symbols + digits

        # define grammar
        word = Word(word_chars)
        delim = CharsNotIn(word_chars)
        delim_and_word = Group(Suppress(Optional(delim)) + word)
        content = ZeroOrMore(delim_and_word) # 'content' is a grammar object.

        self.parser = content.parseString

    def get_wordlist(self, article_string):
        parsed_data = self.parser(article_string)
        word_list = [group[0] for group in parsed_data]
        return word_list

    def init_latex_parser(self):
        # these variables will be used to define valid lists of characters
        lowers = 'qwertyuiopasdfghjklzxcvbnm'
        uppers = lowers.upper()
        alphas = lowers + uppers
        digits = '1234567890'
        other_word_symbols = '-_'
        word_chars = alphas + other_word_symbols + digits
        punctuation_symbols = '.!?:;…'
        command_symbol = '\\'
        white_characters = CharsNotIn(word_chars + punctuation_symbols + command_symbol)

        # define grammar
        word = Word(word_chars)
        command = command_symbol + OneOrMore(alphas) # as far as i can tell, only alphas are allowed in a latex command (bar the special commands such as \&).
        punc = Word(punctuation_symbols)
        white_and_word = Group(Suppress(Optional(white_characters)) + word)
        white_and_command = Group(Suppress(Optional(white_characters)) + command)
        white_and_punc = Group(Suppress(Optional(white_characters)) + punc)
        sentence = ZeroOrMore(white_and_word) + white_and_punc
        pure_piece = ZeroOrMore(sentence)
        bracketed_piece = '{' + pure_piece + Suppress(ZeroOrMore(white_characters)) + '}'

        self.parser = content.parseString
