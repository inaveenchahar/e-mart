from django.contrib import admin
from .models import Cart, CartProduct
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'added_on', 'updated_on', 'completed']


admin.site.register(Cart, CartAdmin)


class CartProductAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'added_on', 'updated_on']


admin.site.register(CartProduct, CartProductAdmin)
