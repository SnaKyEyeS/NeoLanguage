import re
import click
import pyperclip as clipboard


@click.group()
def cli():
    """Small CLI to deeply annoy your friends."""
    pass


@cli.command()
@click.option('-i', '--input', default=clipboard.paste(), help='Input text to invert, if not specified: takes the clipboard\'s content.')
def write(input):
    """Inverts the input string following Noé's rules."""
    tokens = re.split('(\W)', input)

    result = list()
    for token in tokens:
        if token.isalpha():
            token = token[1:][::-1]                 # Remove first letter (1) and reverse (2)
            token = token.replace('i', 'ii')        # Double the i's (3)
            if len(token) > 1:
                token = token[1::-1] + token[2:]    # Invert the first two letters (4)
            token = token.replace('a', '')          # Remove the a's (5)
        result.append(token)
    result = ''.join(result)

    clipboard.copy(result)
    click.secho('Aaaand the result is: ', fg='green', nl=False, bold=True)
    click.secho(result, bold=True)
    click.secho('The result was automatically copied to your clipboard :-)', fg='red')


@cli.command()
@click.argument('text')
def read(text):
    """Reads and translates the input text following Noé's rules."""
    click.echo(text)


if __name__ == '__main__':
    cli()
