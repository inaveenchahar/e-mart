from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='cart user')
    ordered_on = models.DateTimeField(null=True, blank=True, help_text='Cart Ordered by user on')
    cart_value = models.FloatField(default=0, help_text='Cart price')
    delivery_charges = models.IntegerField(default=40)
    completed = models.BooleanField(default=False, help_text='Mark this is user paid for this cart')
    shipped = models.BooleanField(default=False, help_text='Mark if cart products are shipped')
    shipped_on = models.DateField(blank=True, null=True)
    delivered = models.BooleanField(default=False, help_text='Mark if cart products are Delivered')
    delivered_on = models.DateField(blank=True, null=True, help_text='Cart products delivered on')
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='Product name')
    quantity = models.IntegerField(default=1, help_text='Product quantity')
    price = models.FloatField(null=True, help_text='Product price')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cart) + ' - ' + str(self.product.title)

    class Meta:
        ordering = ['-added_on']
