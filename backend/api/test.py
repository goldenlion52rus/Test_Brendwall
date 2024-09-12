from django.test import RequestFactory, TestCase
from django.urls import reverse

from .models import Product
from .views import CreateProductView, ProductView, add_product


class ProductViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = ProductView.as_view()

    def test_get_empty_queryset(self):
        request = self.factory.get(reverse('products'))
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_get_queryset_with_data(self):
        Product.objects.create(title='Product 1',
                               description='Desc 1', price=10.00)

        request = self.factory.get(reverse('products'))
        response = self.view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Product 1')
        self.assertEqual(response.data[0]['price'], 10.00)

    def test_create_product(self):
        data = {'title': 'Product 2', 'description': 'Desc 2', 'price': 20.00}
        request = self.factory.post(reverse('products'), data=data)
        response = self.view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Product 2')
        self.assertEqual(response.data['price'], 20.00)
        self.assertEqual(Product.objects.count(), 1)

    def test_create_product_invalid_price(self):
        data = {'title': 'Product 3', 'description': 'Desc 3', 'price': -10.00}
        request = self.factory.post(reverse('products'), data=data)
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('price' in response.data)
        self.assertIn('Цена должна быть положительным числом',
                      response.data['price'][0])

    def test_create_product_invalid_title(self):
        data = {'title': '', 'description': 'Desc 4', 'price': 15.00}
        request = self.factory.post(reverse('products'), data=data)
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('title' in response.data)
        self.assertIn('Длина заголовка должна составлять не менее 1 символа',
                      response.data['title'][0])


class CreateProductViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = CreateProductView.as_view()

    def test_create_product(self):
        data = {'title': 'Product 4', 'description': 'Desc 4', 'price': 30.00}
        request = self.factory.post(reverse('create-product'), data=data)
        response = self.view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Product 4')
        self.assertEqual(response.data['price'], 30.00)
        self.assertEqual(Product.objects.count(), 1)

    def test_create_product_invalid_price(self):
        data = {'title': 'Product 5', 'description': 'Desc 5', 'price': -20.00}
        request = self.factory.post(reverse('create-product'), data=data)
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('price' in response.data)
        self.assertIn('Цена должна быть положительным числом',
                      response.data['price'][0])

    def test_create_product_invalid_title(self):
        data = {'title': '', 'description': 'Desc 6', 'price': 15.00}
        request = self.factory.post(reverse('create-product'), data=data)
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('title' in response.data)
        self.assertIn('Длина заголовка должна составлять не менее 1 символа',
                      response.data['title'][0])


class AddProductViewTests(TestCase):

    def test_render_template(self):
        request = self.factory.get(reverse('add-product'))
        response = add_product(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
