from django.test import TestCase
from django.urls import reverse
from .models import Product
# Create your tests here.

class ProductModelTest(TestCase):
    def setUp(self):
        # Создаём тестовые данные
        self.product = Product.objects.create(name='Product1', price=99.99)

    def test_product_creation(self):
        # Проверяем, что продукт был создан
        self.assertEqual(self.product.name, 'Product1')
        self.assertEqual(self.product.price, 99.99)

    def test_str_method(self):
        # Проверяем метод __str__ модели
        self.assertEqual(str(self.product), 'Product1')


class ProductViewTest(TestCase):
    def setUp(self):
        # Создаём тестовые данные
        self.product = Product.objects.create(name='Product1', price=99.99)
        self.url = reverse('product_list')  # Замените на реальный URL

    def test_product_list_view(self):
        # Отправляем GET-запрос
        response = self.client.get(self.url)

        # Проверяем, что ответ имеет статус 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Проверяем, что продукт отображается на странице
        self.assertContains(response, 'Product1')
