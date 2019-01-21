# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cart, CartItem
from django.contrib import admin

# Register your models here.

class cart(admin.ModelAdmin):
    list_display = ['id', 'Total', 'updated']
    class meta:
        model = Cart


class Cartitem(admin.ModelAdmin):
    list_display = ['product', 'updated']

    class meta:
        model = CartItem

admin.site.register(Cart, cart)
admin.site.register(CartItem)