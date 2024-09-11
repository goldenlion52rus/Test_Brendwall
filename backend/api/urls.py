from django.urls import path

from .views import CreateProductView, ProductView, add_product

urlpatterns = [
    path('api/products/', ProductView.as_view(), name='products'),
    path('api/create-product/', CreateProductView.as_view(),
         name='create_product'),
    path('', add_product),
]
