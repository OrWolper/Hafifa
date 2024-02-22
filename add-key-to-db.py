import os
from dotenv import load_dotenv
from utils.dbconnection import DbConnection

load_dotenv()

# Define your connection parameters
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
SSL_MODE = os.getenv('SSL_MODE')

def main(key = None, project_name = None):
    """
       Add a new key to the database
    """

    if not key:
        raise Exception('Key is missing')
    
    if not project_name:
        raise Exception('Project name is missing')

    dbConnection = DbConnection(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, SSL_MODE)
    print('Getting key data...')
    sys_id = dbConnection.get_system_id(project_name)
    project_id = dbConnection.get_project_id(sys_id)
    print('Adding key...')
    dbConnection.add_new_key(sys_id, project_id, key)
    print('Key was added successfully!')

if __name__ == "__main__":
    main()
