from django.db import models

# Create your models here.
class ProductData(models.Model):
    Name = models.CharField(max_length=100)
    Img = models.CharField(max_length=100)
    desc = models.TextField()
    stock = models.CharField(max_length=100, default=100)
    price = models.CharField(max_length=100)
    owner = models.CharField(max_length=50, default='Google')
    rating = models.CharField(max_length=5, default=4)

    def __str__(self):
        return self.Name

    