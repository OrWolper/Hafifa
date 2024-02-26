import click

@click.command()
@click.option('--ten', '-t', help='Tenant ID')

def main(ten = None):
    """
       Add new key to the database
    """

    print("hello world")
    print(ten)

if __name__ == '__main__':
    main()