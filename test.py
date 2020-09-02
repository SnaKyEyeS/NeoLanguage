import src.translate as translate
import src.token as token


text = 'Bonjour, je m\'appelle Gilles Poncelet. Mes amis me connaissent sous le nom de JYL, et c\'est très con...'

tokens_fr = token.tokenize_fr(text)
translation = translate.fr_to_neo(tokens_fr)
tokens_neo = token.tokenize_neo(translation)

for t in tokens_neo:
    print(t)
