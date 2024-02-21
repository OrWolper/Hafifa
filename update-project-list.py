import json
import yaml
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

ISSUE_TEMPLATE_FILE_PATH = './.github/ISSUE_TEMPLATE/request-subscription-key.yml'

def yaml_to_json(yaml_text):
    # Parse YAML text
    data = yaml.safe_load(yaml_text)

    # Convert YAML data to JSON
    json_data = json.dumps(data)

    return json_data


def get_issues_template_file_content():
    with open(ISSUE_TEMPLATE_FILE_PATH, 'r', encoding='utf-8') as file:
        return file.read()


def update_issue_template_file_content(content):
    with open(ISSUE_TEMPLATE_FILE_PATH, "w", encoding="utf-8") as file:
        file.write(content)

def update_issue_template(project_list):
    print('Updating issue template...')
    print('Reading issue template file...')
    issue_file_content = get_issues_template_file_content()
    json_template = json.loads(yaml_to_json(issue_file_content))
    projects_object = [object for object in json_template['body']
                    if object['id'] == 'project-name'][0]
    projects_object['attributes']['options'] = project_list
    issue_yaml = yaml.dump(json_template, sort_keys=False)
    print('Updating issue template file...')
    update_issue_template_file_content(issue_yaml)

def main():
    dbConnection = DbConnection(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, SSL_MODE)
    project_list = dbConnection.get_projects_names()
    update_issue_template(project_list)

if __name__ == "__main__":
    main()
