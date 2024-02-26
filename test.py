import click

@click.command()
@click.option('--ten', '-t', help='Tenant ID')
@click.option('--pen', '-p', help='Penant ID')

def main(ten = None, pen = None):
    """
       Add new key to the database
    """

    print("hello world")
    print(ten)
    print(pen)

if __name__ == '__main__':
    main()