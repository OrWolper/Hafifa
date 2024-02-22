
import json as JSON
import requests


class MicrosoftAPIAgent:
    """
        My custom Microsoft API Agent
    """

    def __init__(self, tenant_id, client_id, client_secret):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

    def get_microsoft_token(self):
        """
            Get Microsoft token
        """

        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"

        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "resource": "https://management.azure.com/"
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.request("POST", url, headers=headers, data=data, timeout=30)

        return response.json()["access_token"]

    def create_subscription_key(self, subscription_id, apim_rg_name, apim_name, product_id_name, display_name, id_name):
        """
            Create subscription key for the user
        """
        url = "https://management.azure.com/api/invoke"

        data = {
            "properties": {
                "displayName": display_name,
                "scope": f"/subscriptions/{subscription_id}/resourceGroups/{apim_rg_name}/providers/Microsoft.ApiManagement/service/{apim_name}/products/{product_id_name}",
                "state": "active",
                "allowTracing": False
            }
        }

        headers = {
            "Authorization": f"Bearer {self.get_microsoft_token()}",
            "Content-Type": "application/json",
            "x-ms-path-query": f"/subscriptions/{subscription_id}/resourceGroups/{apim_rg_name}/providers/Microsoft.ApiManagement/service/{apim_name}/subscriptions/{id_name}/?api-version=2022-04-01-preview&notify=true"
        }

        response = requests.request(
            "PUT", url, headers=headers, data=JSON.dumps(data), timeout=30)

        return response.json()
