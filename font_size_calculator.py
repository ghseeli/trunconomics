import pygame
import string

class FontSizeCalculator:
    def __init__(self):
        pygame.font.init()
        
    def size_of_string(self, font_filepath, st):
        font = pygame.font.Font(font_filepath,12)
        (width, height) = font.size(st)
        return {"width": width, "height": height}

    def size_of_many_strings(self, font_filepath, strs):
        return {st: self.size_of_string(font_filepath,st) for st in strs}

    def size_of_all_characters(self, font_filepath):
        all_chars = string.printable
        char_list = list(all_chars)
        return self.size_of_many_strings(font_filepath, char_list)


        
