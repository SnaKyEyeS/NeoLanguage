import src.token as token
import src.translate as translate


base_path = '/media/jyl/MEMJYL/data/'

i = 0
with open(base_path + 'corpus-full.fr', 'r') as corpus, open(base_path + 'corpus-prepped.fr', 'w') as fr, open(base_path + 'corpus-prepped.neo', 'w') as neo:
    line = corpus.readline()

    while line:
        tokens = token.tokenize_fr(line)
        for sentence in tokens:
            line_neo = ''.join(translate.fr_to_neo_line(sentence))
            line_fr = ''.join(sentence)

            neo.write(line_neo)
            fr.write(line_fr)

        line = corpus.readline()

print('Done !')
