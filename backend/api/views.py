from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer


def add_product(request):
    return render(request, 'index.html')
