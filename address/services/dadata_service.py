from asgiref.sync import async_to_sync
from dadata import DadataAsync
from django.conf import settings
from rest_framework.exceptions import APIException


class BaseDadataSearch:
    api_key = None
    secret = None

    def __init__(self):
        self._set_api_key()

    def _set_api_key(self):
        self.api_key, self.secret = settings.DADATA_API_KEYS


class DaDataSearch(BaseDadataSearch):
    @async_to_sync
    async def get_address(self, query, count=10):
        if not self.api_key:
            raise APIException("Не удалось получить ключ")
        async with DadataAsync(self.api_key, self.secret) as dadata:
            address_data = await dadata.suggest(name="address", query=query, count=count)
            return address_data

