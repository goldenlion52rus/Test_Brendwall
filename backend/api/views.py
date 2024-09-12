from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    """Вьюха для получения списка всех товаров."""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CreateProductView(CreateAPIView):
    """Вьюха для создания нового товара."""

    serializer_class = ProductSerializer


def add_product(request):
    """Вьюха для получения главной страницы приложения."""
    return render(request, 'index.html')
