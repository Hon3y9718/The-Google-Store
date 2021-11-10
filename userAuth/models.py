from typing import Match
from django.db import models
from django.db.models.base import Model

# Create your models here.
class UserAddress(models.Model):
    name = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    state = models.CharField(max_length=50)
    Address_Type = models.CharField(max_length=6)
    userId = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CartData(models.Model):
    productId = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    userId = models.CharField(max_length=1000)

    def __str__(self):
        return self.userId

class UserOrders(models.Model):
    productId = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    addressId = models.CharField(max_length=1000)
    userId = models.CharField(max_length=100)

    def __str__(self):
        return self.userId
    