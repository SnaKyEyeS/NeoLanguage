import click
import pyperclip as clipboard

import src.translate as translate


@click.group()
def cli():
    """Small CLI to deeply annoy your friends."""
    pass


@cli.command()
@click.option('-t', '--text', default=clipboard.paste(), help='Input text to invert, if not specified: takes the clipboard\'s content.')
def write(text):
    """Inverts the input string following Noé's rules."""
    translation = translate.fr_to_neo(text)

    clipboard.copy(translation)
    click.secho('Aaaand the result is: ', fg='green', nl=False, bold=True)
    click.secho(translation, bold=True)
    click.secho('The result was automatically copied to your clipboard :-)', fg='red')


@cli.command()
@click.option('-t', '--text', default=clipboard.paste(), help='Input text to invert, if not specified: takes the clipboard\'s content.')
def read(text):
    """Reads and translates the input text following Noé's rules."""
    translation = translate.neo_to_fr(text)

    click.secho('Aaaand the result is: ', fg='green', nl=False, bold=True)
    click.secho(translation, bold=True)
    click.secho('The result was automatically copied to your clipboard :-)', fg='red')


if __name__ == '__main__':
    cli()
