import click
from sort import insertion_sort


@click.group()
def cli():
    pass


@cli.command()
@click.option('--desc', is_flag=True, help='Sorts descending')
@click.option('--alg', type=click.Choice(['insertion']), default='insertion',
              help='The algorithm for sorting. Default: insertion')
@click.argument('values', nargs=-1, type=int)
def sort(desc, values, alg):
    """
    Sorts a list of numbers in ascending form
    """
    values = list(values)
    algorithms = {'insertion': insertion_sort}
    algorithms[alg](values, desc)
    print(values)


if __name__ == '__main__':
    cli()
