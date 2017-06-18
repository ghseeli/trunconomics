""" This shows how to fetch wikipedia articles: https://pypi.python.org/pypi/mediawikiapi/1.0
The documentation is here: https://github.com/lehinevych/MediaWikiAPI/tree/master/docs/source (or actually, you should build it with sphinx if you really want to see it correctly)
"""
import mediawikiapi as wiki

article_name = "Riemann series theorem"
article = wiki.page(article_name)
content = article.content

print(content)
