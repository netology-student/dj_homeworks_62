
import django_filters.rest_framework

from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

class MyResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = MyResultsSetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = MyResultsSetPagination

    # при необходимости добавьте параметры фильтрации
    # https://www.django-rest-framework.org/api-guide/filtering/

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['products']