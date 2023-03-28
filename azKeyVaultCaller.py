# Example code that uses "az login" to authenticate and authorize access to your Keyvault from a py script
# Remember: DO NOT LOG YOUR SECRETS
from azure.core.exceptions import ClientAuthenticationError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def getAzKvSecret(vaultURL,secretName):

    # additionally_allowed_tenants parameter is needed when working on trial Azure subs as users may use their live.com id to access the tenant
    # exclude_shared_token_cache_credential is needed because there maybe expired tokens in cache. IDKW.
    credential = DefaultAzureCredential(additionally_allowed_tenants=['*'], exclude_shared_token_cache_credential=True)
    try:
        secret_client=SecretClient(vault_url=vaultURL, credential=credential)
        secret = secret_client.get_secret(secretName)
    except ClientAuthenticationError as ex:
        print(ex.message)
        print ("*** Did you do az login? ***")

    return secret
    
# To use, either import this module and call the function, or uncomment the lines below to run directly
#secret=getAzKvSecret("YOUR_KEYVAULT_URL", "YOUR_SECRET_NAME")
#print(secret.value)
