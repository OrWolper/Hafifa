import os
import click
from dotenv import load_dotenv
from utils.dbconnection import DbConnection

load_dotenv()

# Define your connection parameters
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
SSL_MODE = os.getenv('SSL_MODE')

@click.command()
@click.option('--project-name', '-pn', help='Project Name')
@click.option('--key', '-k', help='Subscription Key')
@click.option('--is-prod', '-ip', help='Is the project is prod')

def main(project_name = None, key = None, is_prod = None):
    """
       Add new key to the database
    """

    if not project_name:
        raise Exception('Project name is missing')

    if not key:
        raise Exception('Key is missing')

    if not is_prod:
        raise Exception('Is prod is missing')

    dbConnection = DbConnection(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, SSL_MODE)
    dbConnection.add_new_key(project_name, key, is_prod)

if __name__ == "__main__":
    main()
