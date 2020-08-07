from django.shortcuts import render

# Create your views here.
from httpx import HTTPError
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from address.services.dadata_service import DaDataSearch


class AddressSearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        query = request.query_params.get('query', '')
        count = request.query_params.get('count', 10)
        dadata_service = DaDataSearch()
        try:
            address_data = dadata_service.get_address(query, count)
            return Response(address_data)
        except HTTPError as e:
            sc = e.response.status_code
            if sc == 403:
                return Response('Превышено колличество запросов в день', 403)
            elif sc == 413:
                return Response('Превышено колличество символов в запросе', 413)
