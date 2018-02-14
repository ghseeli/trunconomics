from config import *
from fetch import Article
from parse import ArticleReader()

def main():
    # set up things
    word = 'mountain'
    article = Article('Mount Everest', 'wiki')
    reader = ArticleReader()
    word_list = reader.get_word_list(article.content)
    association_radius = 5
    strong_threshold = None
    weak_theshold = None
    # do
    assoc_dic = AssocDic(association_radius, [word_list])
    print(json.dumps(assoc_dic.assoc_dic, indent=4))
    potential_synonyms = get_potential_synonyms(word_list, assoc_dic, word, strong_threshold, weak_theshold)
    synonyms = weed_out_synonyms(word, potential_synonyms)
    print(synonyms)

if __name__ == '__main__':
    main()
