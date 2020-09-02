import src.translate as translate
import src.token as token


tokens1 = translate.fr_to_neo('Bonjour, je m\'appelle Gilles Poncelet. Mes amis me connaissent sous le nom de JYL, et c\'est très con...')

for t in tokens1:
    print(t)

tokens2 = token.tokenize_neo(translate.format(tokens1))
for t in tokens2:
    print(t)
