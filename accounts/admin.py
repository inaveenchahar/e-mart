from django.contrib import admin
from .models import UserProfile, UserAddress

# Register your models here.

admin.site.register(UserProfile)


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone_no', 'pincode', 'added_on', 'updated_on']


admin.site.register(UserAddress, UserAddressAdmin)
