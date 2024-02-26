from azure.identity import ClientSecretCredential
from azure.mgmt.apimanagement import ApiManagementClient
from azure.mgmt.apimanagement.models import SubscriptionCreateParameters

class AzureManagement:
    def __init__(self, client_id, client_secret, tenant_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
    
    def credentials(self):
        return ClientSecretCredential(
            client_id=self.client_id,
            client_secret=self.client_secret,
            tenant_id=self.tenant_id,
            authority=f"https://login.microsoftonline.com/{self.tenant_id}"
        )
    
    def api_management_client(self, subscription_id):
        return ApiManagementClient(
            credentials=self.credentials(),
            subscription_id=subscription_id
        )
    
    def subscription_create_parameters(self, resource_group_name, service_name, subscription_id, product_id, display_name):
        return SubscriptionCreateParameters(
            scope=f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/products/{product_id}",
            display_name=display_name,
            # product_id=product_id,
            allow_tracing=False,
            state="active"
        )
    
    def creat_subscription(self, resource_group_name, service_name, subscription_id, product_id, display_name):
        return self.api_management_client(subscription_id).subscription.create_or_update(
            resource_group_name=resource_group_name,
            service_name=service_name,
            subscription_id=subscription_id,
            parameters=self.subscription_create_parameters(resource_group_name, service_name, subscription_id, product_id, display_name)
        )




# Azure subscription ID, resource group, API Management service name, and tenant ID
subscription_id = '<subscription_id>'
resource_group_name = '<resource_group_name>'
service_name = '<service_name>'
tenant_id = '<tenant_id>'

# Application (client) ID, client secret, and Azure Active Directory (AAD) endpoint
client_id = '<client_id>'
client_secret = '<client_secret>'
aad_endpoint = 'https://login.microsoftonline.com/'

# Initialize the Service Principal credentials
credentials = ClientSecretCredential(
    client_id=client_id,
    client_secret=client_secret,
    tenant_id=tenant_id,
    authority=aad_endpoint + tenant_id
)

# Initialize the API Management client
api_management_client = ApiManagementClient(
    credentials=credentials,
    subscription_id=subscription_id
)

# Define subscription parameters
subscription_id = '<subscription_id>'
scope = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}"
owner_id = '<owner_id>'  # The user or group ID who owns the subscription
product_id = '<product_id>'  # The product ID associated with the subscription

# Create subscription parameters object
subscription_create_parameters = SubscriptionCreateParameters(
    scope=scope,
    owner_id=owner_id,
    product_id=product_id,
    allow_tracing=False,
    state='active'
)

# Create subscription
subscription = api_management_client.subscription.create_or_update(
    resource_group_name=resource_group_name,
    service_name=service_name,
    subscription_id='<subscription_id>',  # Unique ID for the subscription
    parameters=subscription_create_parameters
)

print("Subscription created successfully:")
print(subscription)