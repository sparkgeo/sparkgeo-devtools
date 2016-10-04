__version__ = '0.0.1'

import click
from sparkgeo.context import CommandContext


pass_context = click.make_pass_decorator(CommandContext, ensure=True)
