from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from accounts.models import UserAddress
# Create your models here.


#  An order is created when a user pays for a session
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, help_text='select cart to which order will be created')
    order_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Username')
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, limit_choices_to={'default_address': True}, blank=True, null=True, help_text='Delivery address, only default can be selected')
    order_id = models.CharField(max_length=255, help_text='Order id will be created by razorpay automatically')
    note = models.CharField(max_length=100, blank=True)
    order_amount = models.IntegerField(verbose_name='Order Amount', help_text='Amount in paisa(1 Rs = 100 paise')
    completed = models.BooleanField(default=False, help_text='Payment for this order is completed')
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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='Select order for payment')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='created', help_text='Payment status')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Payment done by user')
    transaction_id = models.CharField(max_length=255, blank=True, help_text='Transaction id will be created by razorpay automatically')
    currency = models.CharField(max_length=10, help_text='Payment currency')
    signature = models.CharField(max_length=255, blank=True, help_text='Automatically created by razorpay')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order)
