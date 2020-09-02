import re
import click
import pyperclip as clipboard

import src.translate as translate
import src.token as token


@click.group()
def cli():
    """Small CLI to deeply annoy your friends."""
    pass


@cli.command()
@click.option('-i', '--input', default=clipboard.paste(), help='Input text to invert, if not specified: takes the clipboard\'s content.')
def write(input):
    """Inverts the input string following Noé's rules."""
    tokens = token.tokenize_fr(input)

    print(tokens)

    translation = translate.fr_to_neo(tokens)

    clipboard.copy(translation)
    click.secho('Aaaand the result is: ', fg='green', nl=False, bold=True)
    click.secho(translation, bold=True)
    click.secho('The result was automatically copied to your clipboard :-)', fg='red')


@cli.command()
@click.argument('text')
def read(text):
    """Reads and translates the input text following Noé's rules."""
    click.echo(text)


if __name__ == '__main__':
    cli()
