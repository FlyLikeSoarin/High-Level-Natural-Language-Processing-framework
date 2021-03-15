import os

import click


@click.group()
def cli():
    pass


@cli.command()
def init():
    if not os.listdir('.'):
        print('Creating new odin project...')
        with open('settings.py', 'w'):
            pass
        os.mkdir('flows')
        os.mkdir('models')
        os.mkdir('__schemas__')
        print('Project successfully created!')
    else:
        print('Error: project can only be initialized in empty folder!')


def run():
    cli()


if __name__ == '__main__':
    cli()
