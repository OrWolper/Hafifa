import click
from utils.microsoftapi import MicrosoftAPIAgent
from utils.m import AzureManagement

# TODO - add user_id

@click.command()
@click.option('--tenant-id', '-t', help='Tenant ID')
@click.option('--subscription-id', '-s', help='Subscription ID')
@click.option('--apim-rg-name', '-rg', help='APIM Resource Group Name')
@click.option('--apim-name', '-n', help='APIM Name')
@click.option('--client-id', '-c', help='Client ID')
@click.option('--client-secret', '-cs', help='Client Secret')
@click.option('--subscription-key-name', '-i', help='Subscription Key Name')
@click.option('--product-name', '-p', help='Product Name')

def main(tenant_id=None, subscription_id=None, apim_rg_name=None, apim_name=None, client_id=None, client_secret=None, subscription_key_name=None, product_name=None):
    """
        Create new subscription key
    """
    print(
        f"subscription_id: {subscription_id} \napim_rg_name: {apim_rg_name} \napim_name: {apim_name} \nclient_id: {client_id}\ntenant_id: {tenant_id}\n subscription_key_name: {subscription_key_name}\n product_name: {product_name}")

    if not tenant_id:
        raise Exception('Tenant ID is missing')

    if not subscription_id:
        raise Exception('Subscription ID is missing')

    if not apim_rg_name:
        raise Exception('APIM Resource Group Name is missing')

    if not apim_name:
        raise Exception('APIM Name is missing')

    if not client_id:
        raise Exception('Client ID is missing')

    if not client_secret:
        raise Exception('Client Secret is missing')

    if not subscription_key_name:
        raise Exception('Subscription Key Name is missing')
    
    if not product_name:
        raise Exception('Product Name is missing')
    
    microsoft_api = MicrosoftAPIAgent(tenant_id, client_id, client_secret)
    microsoft_api.create_subscription_key(subscription_id, apim_rg_name, apim_name, product_name, subscription_key_name, id_name = None)

    azure_management = AzureManagement(tenant_id, client_id, client_secret)
    azure_management.creat_subscription(apim_rg_name, apim_name, subscription_id, product_name, subscription_key_name, id_name = None)

    print(f"Subscription Key {subscription_key_name} created successfully")

if __name__ == '__main__':
    main()