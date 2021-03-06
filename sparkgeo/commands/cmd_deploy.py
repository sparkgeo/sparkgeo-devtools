import json
from sparkgeo import pass_context, create_group


# Required for dynamic import
cli = create_group(
    'deploy', 'Build commands for use with different platforms, such as: Docker, Go, Python'
)

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


@cli.command()
@pass_context
def create_eb_archive(ctx):
    """Build an archive for deploying to Elastic Beanstalk"""
    pass


@cli.command()
@pass_context
def deploy_eb_version(ctx):
    """Create a new version and update Elastic Beanstalk"""
    pass
