# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products.models import product
from django.db import models
from django.conf import settings

# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True)
    product = models.ForeignKey(product, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=19.99, max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title

class Cart(models.Model):
    #item = models.ManyToManyField(CartItem, null=True, blank=True)
    #products = models.ManyToManyField(product, null=True, blank=True)
    Total = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "cart id: %s" %(self.id)
