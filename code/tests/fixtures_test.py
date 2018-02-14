from assoc_dic import *

basic_word_list1 =  ['The','quick','red','fox','jumped','over','the','brown','dog']
basic_word_list2 = ['Conditional', 'and', 'unconditional', 'convergence', 'Operator', 'Theory', 'Advances', 'Basel', 'and', 'Applications', '94', 'Translated', 'by', 'Andrei', 'Iacob', 'from', 'the', 'and', 'Russian-language', 'Basel', 'Birkh', 'user', 'Verlag', 'pp', 'viii', '156', 'ISBN', '3-7643-5401-1', 'MR', '1442255', 'Weisstein', 'Eric', '2005', 'Riemann', 'Series', 'Theorem', 'Retrieved', 'May', '16', '2005']
basic_sentence = 'bla bla the characteristic of a field is p    The char of a field is p'

class LazyAssocDic:
    def __init__(self, radius, corpus):
        self.assoc_dic = None
        self.r = radius
        self.c = corpus
        
    def get_dict(self):
        if self.assoc_dic is None:
            self.assoc_dic = AssocDic(self.r, self.c)
        return self.assoc_dic

dic_gen = LazyAssocDic(2,[basic_word_list1])

