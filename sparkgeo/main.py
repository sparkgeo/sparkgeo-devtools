'''
Authors: Michael Connor
Contact: mike@sparkgeo.com

Command Line tools for common deploy and build functions

This is a Click application
Click is the 'Command Line Interface Creation Kit'
Learn more at http://click.pocoo.org/5/

For usage:
    sparkgeo --help

'''
import click

from sparkgeo.command_loader import CommandLoader


# Main command group
@click.command(cls=CommandLoader)
def cli():
    """Sparkgeo Command Line Tools
    example:
        sparkgeo deploy --lang go --name Maptiks-Catcher --env m-catcher-dev
    """
    pass
