import itertools
import src.token as t


def fr_to_neo(text):
    """
    Translates from French to Neo-Language.
    Outputs a list of sentences organized as a list of tokens.
    """
    sentences = t.tokenize_fr(text)
    result = list()

    for sentence in sentences:
        tokens = list()
        for token in sentence:
            if token.isalpha():
                token = token[1:][::-1]                 # Remove first letter (1) and reverse (2)
                token = token.replace('i', 'ii')        # Double the i's (3)
                if len(token) > 1:
                    token = token[1::-1] + token[2:]    # Invert the first two letters (4)
                token = token.replace('a', '')          # Remove the a's (5)
            if token:
                tokens.append(token)
        result.append(tokens)

    return result


def format(output):
    """
    Formats the output so that it is readable by a human.
    """
    for sentence in output:
        sentence.append(' ')
    return ''.join(itertools.chain(*output))
