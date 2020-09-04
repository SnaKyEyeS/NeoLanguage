import sys
import spacy

import src.translate as translate

nlp_fr = spacy.load('fr_core_news_sm')


if __name__ == '__main__':
    path = sys.argv[1]
    corpus_shuffled = f'{path}/corpus-shuffled.fr'
    corpus_prep_fr = f'{path}/corpus-prep.fr'
    corpus_prep_neo = f'{path}/corpus-prep.neo'

    with open(corpus_shuffled, 'r') as corpus, open(corpus_prep_fr, 'w') as fr, open(corpus_prep_neo, 'w') as neo:
        i = 0
        line = corpus.readline()
        while line:
            try:
                line = nlp_fr(line)
            except Exception:
                line = corpus.readline()
                continue

            for sentence in line.sents:
                line_fr = sentence.text.lower()
                line_neo = ''.join(translate.fr_to_neo_line(line_fr))

                fr.write(line_fr)
                neo.write(line_neo)

            if i % 1e5 == 0:
                print(f'Currently at line n°{i}...')
            i += 1
            line = corpus.readline()
