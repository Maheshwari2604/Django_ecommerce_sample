# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import os
from django.utils.safestring import mark_safe

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)
    slug = models.SlugField(unique = True)
    #Image = models.FileField(upload_to='products/images/', null= True)   
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class productImage(models.Model):
    Product = models.ForeignKey(product)
    image = models.ImageField(upload_to='products/images/', blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.Product.title
