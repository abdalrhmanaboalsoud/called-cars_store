from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

class CarViewTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@example.com',
            password='password123'
        )

        self.car = Car.objects.create(
            brand='Toyota',
            model='Corolla',
            price=20000,
            is_bought=True,
            buyer_id=self.user  # Corrected field name here
        )

    def test_list_page_status_code(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_details_view(self):
        url = reverse('car_details', args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_details.html')

    def test_create_view(self):
        url = reverse('create_car')
        response = self.client.post(url, {
            'brand': 'Honda',
            'model': 'Civic',
            'price': 22000,
            'is_bought': True,
            'buyer_id': self.user.id  # Corrected field name here
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('car_details', args=[Car.objects.last().id]))

    def test_update_view(self):
        url = reverse('car_update', args=[self.car.id])
        response = self.client.post(url, {
            'brand': 'Toyota',
            'model': 'Camry',
            'price': 25000,
            'is_bought': True,
            'buyer_id': self.user.id  # Corrected field name here
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        updated_car = Car.objects.get(id=self.car.id)
        self.assertEqual(updated_car.model, 'Corolla')

    def test_delete_view(self):
        url = reverse('car_delete', args=[self.car.id])
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 0)
