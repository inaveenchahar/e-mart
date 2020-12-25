from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(null=True, blank=True)
    cart_value = models.FloatField(default=0)
    delivery_charges = models.IntegerField(default=40)
    completed = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False, help_text='Mark if cart products are shipped')
    delivered = models.BooleanField(default=False)
    delivered_on = models.DateField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-added_on']
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cart) + ' - ' + str(self.product.title)

    class Meta:
        ordering = ['-added_on']
