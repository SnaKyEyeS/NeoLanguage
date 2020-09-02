import re
import spacy

nlp_fr = spacy.load('fr_core_news_sm')
nlp_neo = spacy.load('fr_core_news_sm')


def neo_boundaries(doc):
    separators = ['.', '!', '?', '...']
    for token in doc[:-1]:
        t = token.text
        if t in separators:
            doc[token.i+1].is_sent_start = True
    return doc


nlp_neo.add_pipe(neo_boundaries, before='parser')


def tokenize_fr(text):
    """
    Takes a french text and outputs a list of tokens.
    """
    text = nlp_fr(text)
    sentences = list()

    for sentence in text.sents:
        tokens = [token.lower() for token in re.split('(\\W)', sentence.text) if token]
        sentences.append(tokens)

    return sentences


def tokenize_neo(text):
    """
    Takes a neo text and outputs a list of tokens.
    """
    text = nlp_fr(text)
    sentences = list()

    for sentence in text.sents:
        tokens = [token.lower() for token in re.split('(\\W)', sentence.text) if token]
        sentences.append(tokens)

    return sentences
