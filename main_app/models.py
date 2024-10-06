from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    product = models.ManyToManyField('Product', related_name='products')
