import sys
import json
import click


class CommandContext(object):
    """
    Class to encapsulate common session context for the cli commands.
    """

    # def __init__(self):
    #     self.session = gbdx_auth.get_session()
    #     self.gbdx = Interface(gbdx_connection=self.session)

    # def get(self, url):
    #     return self.session.get(url)
    #
    # def post(self, url, data):
    #     headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    #     return self.session.post(url, data=data, headers=headers)
    #
    # def put(self, url, data):
    #     headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    #     return self.session.put(url, data=data, headers=headers)
    #
    # def delete(self, url):
    #     return self.session.delete(url)

    def log(self, msg, error=False, *args):
        """Logs a message to stdout or stderr."""
        if args:
            msg %= args

        if error:
            click.echo(msg, file=sys.stderr)
        else:
            click.echo(msg, file=sys.stdout)

    def show(self, data, is_json=False, sort=True):
        """Output Formated JSON"""
        if is_json:
            click.echo(json.dumps(data, sort_keys=sort, indent=4, separators=(',', ': ')))
        else:
            click.echo(data)
