from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'visible', 'added_on', 'updated_on']
    search_fields = ['title']
    list_filter = ['visible']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'order', 'visible', 'added_on', 'updated_on']
    search_fields = ['title']
    list_filter = ['visible', 'category']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['price']


admin.site.register(Product, ProductAdmin)

