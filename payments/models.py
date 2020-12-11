from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from accounts.models import UserAddress
# Create your models here.


#  An order is created when a user pays for a session
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, limit_choices_to={'default_address': True}, blank=True, null=True)
    order_id = models.CharField(max_length=255)
    note = models.CharField(max_length=100, blank=True)
    order_amount = models.IntegerField(verbose_name='Order Amount')
    completed = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.order_id


class Payment(models.Model):
    STATUS_CHOICES = (
        (('CREATED', 'created')),
        (('AUTHORIZED', 'authorized')),
        (('CAPTURED', 'captured')),
        (('REFUNDED', 'refunded')),
        (('FAILED', 'failed')),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='created')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=10)
    signature = models.CharField(max_length=255, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order)
