import json
import click
from sparkgeo import pass_context


@click.group()
def deploy():
    """Task commands"""
    pass


# Required for dynamic import
cli = deploy
