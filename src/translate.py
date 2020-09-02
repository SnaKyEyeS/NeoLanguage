import itertools


def fr_to_neo(tokens):
    """
    Translates from French to Neo-Language.
    """
    result = list()

    for sentence in tokens:
        result.append(fr_to_neo_line(sentence))

    return format(result)


def fr_to_neo_line(sentence):
    """
    Translates a list of French tokens into a list of Neo tokens.
    """
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

    return tokens


def format(output):
    """
    Formats the output to be human-readbale
    """
    for sentence in output:
        sentence.append(' ')
    return ''.join(itertools.chain(*output))
