from decimal import Decimal

from django.contrib.auth.models import User
import requests
from django.db import models


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0'))
    user_id = models.CharField(max_length=10)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'


class CartItem(models.Model):
    product_id = models.CharField(max_length=255)
    quantity = models.IntegerField()
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

    def __str__(self):
        return self.product_id
    class Meta:
        db_table = 'cart_item'
        verbose_name = 'CartItem'

    def save(self, *args, **kwargs):
        if self.product_id[0] == 'B':
            self.type = 'Book'
            book_url = 'http://127.0.0.1:1000/api/books/{}'.format(self.product_id)
            response = requests.get(book_url)
            if response.status_code == 200:
                book_data = response.json()
                self.price = Decimal(str(book_data['price']))
        elif self.product_id[0] == 'M':
            self.type = 'Mobile'
            mobile_url = 'http://127.0.0.1:2000/api/mobiles/{}'.format(self.product_id)
            response = requests.get(mobile_url)
            if response.status_code == 200:
                mobile_data = response.json()
                self.price = Decimal(str(mobile_data['price']))
        elif self.product_id[0] == 'C':
            self.type = 'Clothes'
            clothes_url = 'http://127.0.0.1:3000/api/clothes/{}'.format(self.product_id)
            response = requests.get(clothes_url)
            if response.status_code == 200:
                clothes_data = response.json()
                self.price = Decimal(str(clothes_data['price']))
        super(CartItem, self).save(*args, **kwargs)

