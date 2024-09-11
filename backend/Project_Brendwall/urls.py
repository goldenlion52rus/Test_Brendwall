from django.contrib import admin
from django.urls import include, path

from api.views import add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('add-product/', add_product, name='add_product')
]
