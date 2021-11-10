from django.contrib import admin

from userAuth.models import CartData, UserAddress, UserOrders

# Register your models here.
admin.site.register(UserAddress)
admin.site.register(CartData)
admin.site.register(UserOrders)