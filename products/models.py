from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30, help_text='Category name')
    slug = models.SlugField(max_length=30, unique=True)
    order = models.IntegerField(blank=True, help_text='Display order')
    visible = models.BooleanField(default=True, help_text='Visible to users')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_on']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ManyToManyField(Category, help_text='Product will appear in selected categories')
    title = models.CharField(max_length=100, help_text='Product name')
    slug = models.SlugField(max_length=100)
    price = models.FloatField(help_text='Product price')
    order = models.IntegerField(blank=True, help_text='Display order')
    visible = models.BooleanField(default=True, help_text='Visible to users')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_on']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
