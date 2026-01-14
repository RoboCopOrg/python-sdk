import click
from . import sayHello

@click.command()
def cli():
    """CLI command that prints 'hello'"""
    print(sayHello())

