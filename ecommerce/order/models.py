# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cart.models import CartItem, Cart
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned","Abandoned"),
    ("Finished", "Finished"),
)



class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    Order_id = models.CharField(max_length=120, unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices= STATUS_CHOICES, default="STARTED")
    
    sub_total = models.DecimalField(default=19.99, max_digits=10, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    final_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.Order_id