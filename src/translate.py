import re
import spacy
import itertools

from websocket import create_connection

nlp_fr = spacy.load('fr_core_news_sm')


def fr_to_neo(text):
    """
    Translates from French to Neo-Language.
    """
    result = list()
    text = nlp_fr(text)

    for sentence in text.sents:
        result.append(fr_to_neo_line(sentence.text.lower()))

    return format(result)


def fr_to_neo_line(sentence):
    """
    Translates a list of French tokens into a list of Neo tokens.
    """
    tokens = list()

    for token in re.split('(\\W)', sentence):
        if token.isalpha():
            token = token[1:][::-1]                 # Remove first letter (1) and reverse (2)
            token = token.replace('i', 'ii')        # Double the i's (3)
            if len(token) > 1:
                token = token[1::-1] + token[2:]    # Invert the first two letters (4)
            token = token.replace('a', '')          # Remove the a's (5)
        if token:
            tokens.append(token)

    return tokens


def neo_to_fr(text):
    """
    Translates a Neo text to French.
    """
    ws = create_connection("ws://localhost:{}/translate".format(8080))
    ws.send(text)
    return ws.recv()


def format(output):
    """
    Formats the output to be human-readbale
    """
    for sentence in output:
        sentence.append(' ')
    return ''.join(itertools.chain(*output))
