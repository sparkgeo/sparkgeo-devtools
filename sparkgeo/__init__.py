__version__ = '0.0.1'

import click
from sparkgeo.context import *


pass_context = click.make_pass_decorator(CommandContext, ensure=True)


def create_group(name, description):
    """ Create a click group for each sub group of the cli."""
    @click.group(name)
    @add_doc(description)
    def new_group():
        pass

    return new_group


class add_doc(object):
    """Decorator to add a docstring to a function"""
    def __init__(self, description):
        self.doc = description

    def __call__(self, f):
        f.__doc__ = self.doc
        return f
