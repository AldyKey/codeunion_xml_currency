from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Currency
from .serializers import CurrencySerializer
from .utils import CustomPageNumberPagination


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    serializer_class = CurrencySerializer
    pagination_class = CustomPageNumberPagination


class CurrencyRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrencySerializer

    def get_object(self):
        currency = Currency.objects.filter(id=self.kwargs.get('pk')).first()
        return currency
