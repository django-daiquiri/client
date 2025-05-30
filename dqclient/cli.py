import click
from functools import wraps

from .metadata import MetadataCLI
from daiquiri_client import __version__


@click.group(help=f'Command Line Interface for Django-Daiquiri-Client. (Version: {__version__})')
@click.version_option(__version__)
def cli():
    pass


@cli.group(help='Commands for managing the metadata.', invoke_without_command=True)
@click.pass_context
def metadata(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


def common_options(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper = click.option('-h', '--host', required=True, help='Host address')(wrapper)
    wrapper = click.option('-t', '--token', required=True, help='API Token')(wrapper)
    wrapper = click.option(
        '-v',
        '--verbose',
        required=False,
        default=False,
        is_flag=True,
        help='Show verbose output (with tables)',
    )(wrapper)
    return wrapper


@metadata.command('ls', short_help='List metadata (schemas, tables and columns).')
@common_options
def ls(host: str, token: str, verbose: bool = False) -> None:
    MetadataCLI().ls(host, token, verbose)


@metadata.command('push', short_help='Push the metadata from the local file to host.')
@common_options
@click.option(
    '--schemas',
    required=False,
    help='Comma-separated schemas, e.g.,  --schemas name1,name2. Push all if the option is omitted.',
)
@click.option(
    '--tables',
    required=False,
    help='Comma-separated tables, e.g.,  --tables name1,name2. Push all if the option is omitted.',
)
@click.option(
    '-i',
    '--input',
    required=True,
    help='Input file (yaml)',
)
def push(host: str, token: str, verbose: bool, schemas: str, tables: str, input: str) -> None:
    schemas_list = [] if schemas is None else schemas.split(',')
    tables_list = [] if tables is None else tables.split(',')
    MetadataCLI().push(host, token, input, schemas_list, tables_list, verbose)


@metadata.command('pull', short_help='Pull the metadata and save it into a yaml file.')
@common_options
@click.option(
    '--schemas',
    required=False,
    help='Comma-separated schemas, e.g.,  --schemas name1,name2. Pull all if the option is omitted.',
)
@click.option(
    '--tables',
    required=False,
    help='Comma-separated tables, e.g.,  --tables name1,name2. Pull all if the option is omitted.',
)
@click.option(
    '-o',
    '--output',
    required=True,
    help='Output file',
)
def pull(host: str, token: str, verbose: bool, schemas: str, tables: str, output: str) -> None:
    schemas_list = [] if schemas is None else schemas.split(',')
    tables_list = [] if tables is None else tables.split(',')
    MetadataCLI().pull(host, token, output, schemas_list, tables_list, verbose)


if __name__ == '__main__':
    cli()
