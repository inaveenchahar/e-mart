from django.contrib import admin
from .models import Order, Payment
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_by', 'order_id', 'order_amount', 'completed', 'added_on', 'updated_on']


admin.site.register(Order, OrderAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['paid_by', 'order', 'transaction_id', 'status', 'added_on', 'updated_on']


admin.site.register(Payment, PaymentAdmin)
