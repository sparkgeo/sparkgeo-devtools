"""
See Click docs for Custom Multi Commands: http://click.pocoo.org/5/commands/#custom-multi-commands
"""
import click
import os
import sys


plugin_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))

class CommandLoader(click.MultiCommand):

    COMMAND_FILE_PREFIX = 'cmd_'

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and \
               filename.startswith(self.COMMAND_FILE_PREFIX):
                rv.append(filename[len(self.COMMAND_FILE_PREFIX):-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('gbdxcli.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError as e:
            print e
            return
        return mod.cli

cli = CommandLoader(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')

if __name__ == '__main__':
    cli()
