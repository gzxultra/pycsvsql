import click

@click.command()
@click.option('--file', default='sample.csv', prompt='name of your csv file')
def pycsvsql(file):
    print(file)


if __name__ == '__main__':
    pycsvsql()
