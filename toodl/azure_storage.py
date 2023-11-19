# core/azure_storage.py

import os
from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = 'static'
    expiration_secs = None