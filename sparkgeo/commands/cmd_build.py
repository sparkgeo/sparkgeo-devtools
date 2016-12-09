import json
import os
from sparkgeo import pass_context, create_group, click
from sparkgeo import context
from fabric.api import local, cd


# Required for dynamic import
cli = create_group(
    'build', 'Deployment commands for use with different platforms, such as: Elastic Beanstalk, etc'
)

# """EXAMPLES:
# @click.option('--startswith','-s', type=click.STRING,
#     help="Only return tasks that start with this substring")
# @click.option('--filename', '-f', type=click.File('r'),
#     help='Filename of task to register (JSON file)')
# @click.option('--workflow_id','-w', type=click.INT,
#     help="Id of task")
# @click.option('--verbose', '-v', is_flag=True,
#     help='Output a more detailed status of workflow')
#
# @click.argument('id', nargs=1, type=click.INT)
# @click.option('--state', '-s', type=click.Choice([
#         'all', 'submitted', 'scheduled', 'started', 'canceled',
#         'cancelling', 'failed', 'succeeded', 'timedout',
#         'pending','running', 'complete'
#     ]),
#     help='Name of the state to filter by.')
# """


@cli.command()
def get_go_commondevtools():
    """
    Build an archive for deploying to Elastic Beanstalk.


    """
    pass


@cli.command()
def get_gogb_dependencies(subdir):
    """
    Download and install Service Go dependencies.

    :param subdir: The sub directory where the dependencies are to be downloaded to.
    """
    pass


@cli.command()
@click.option('--subdir', '-d',
              type=click.Path(exists=True, file_okay=False, readable=False),
              help="Subdirectory where the go src code is located, if required.")
def goget(subdir):
    """Download Go dependencies."""
    with cd(subdir):
        local("go get -v -d")


@cli.command()
@click.option('--subdir', '-d',
              type=click.Path(exists=True, file_okay=False, readable=False),
              help="Subdirectory where the go src code is located, if required.")
@click.option('--name', '-n',
              type=click.STRING,
              help="Name of the build binary")
def build_go_binary(sub_dir, name):
    """Create a new version and update Elastic Beanstalk."""
    with cd(sub_dir):
        local("""docker run --rm -it \
            -v "/home/ubuntu/.go_workspace":/gopath \
            -v "$(pwd)":/app \
            -e "GOPATH=/gopath" -w /app \
            golang:1.6.3-alpine \
            sh -c 'CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" -o %s'
        """ % name)


@cli.command()
@click.option('--input-file', '-i',
              type=click.File('r'),
              help="Dockerfile name, relative to current working dir")
@click.option('--output-file', '-o',
              type=click.File('w'),
              help="Dockerfile name, relative to current working dir")
@click.option('--attr', '-a',
              type=(str, str), multiple=True,
              help=""
              )
def dockerfile_inject_envvars(input_file, output_file, attr):
    """Substitute the attrs into the dockerfile as env vars.

    This function will iterate through attr, for each tuple, the Dockerfile will be searched for
    %(attr[0])s. If that doesn't exist, no substitutions will be done.
    """
    attrs = dict(attr)

    data = input_file.read() % attrs

    output_file.write(data)


@cli.command()
@click.option('--img-tag', '-t',
              type=click.STRING,
              help="Name of image to build")
@click.option('--img-tag', '-t',
              type=click.STRING,
              help="Name of image to build")
@click.option('--filename', '-f',
              type=click.Path(exists=True),
              help="Dockerfile name, relative to current working dir")
def build_docker_img(img_tag, filename, context):
    """Create a  and update Elastic Beanstalk."""
    if context is None:
        context = '.'
    local("docker build -t %s -f %s --no-cache %s" % (img_tag, filename, context))
