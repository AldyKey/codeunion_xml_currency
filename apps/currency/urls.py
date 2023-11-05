from django.urls import path

from .views import CurrencyListView, CurrencyRetrieveView


urlpatterns = [
    path('', CurrencyListView.as_view(), name='currency_list'),
    path('currency/<int:pk>/', CurrencyRetrieveView.as_view(), name='currency_get')
]
