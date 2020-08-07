from django.urls import path

from .views import AddressSearchView

urlpatterns = [
    path('search/', AddressSearchView.as_view()),
]
