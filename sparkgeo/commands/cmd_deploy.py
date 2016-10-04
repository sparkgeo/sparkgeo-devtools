import json
import click
from sparkgeo import pass_context


@click.group()
def deploy():
    """Task commands"""
    pass


# Required for dynamic import
cli = deploy

"""EXAMPLES:
@click.option('--startswith','-s', type=click.STRING,
    help="Only return tasks that start with this substring")
@click.option('--filename', '-f', type=click.File('r'),
    help='Filename of task to register (JSON file)')
@click.option('--workflow_id','-w', type=click.INT,
    help="Id of task")
@click.option('--verbose', '-v', is_flag=True,
    help='Output a more detailed status of workflow')

@click.argument('id', nargs=1, type=click.INT)
@click.option('--state', '-s', type=click.Choice([
        'all', 'submitted', 'scheduled', 'started', 'canceled',
        'cancelling', 'failed', 'succeeded', 'timedout',
        'pending','running', 'complete'
    ]),
    help='Name of the state to filter by.')
"""


@deploy.command('archive')

@pass_context
def archive(ctx):
    """Build an archive for deploying to Elastic Beanstalk"""
    pass
