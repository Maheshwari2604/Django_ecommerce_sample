# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import product, productImage
from .serializers import productSerializer

# Register your models here.
class productamdin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'timestamp']
    list_editable = ['price', 'active']
    search_fields = ['title', 'description']
    date_hierarchy = 'timestamp'
    list_filter = ['title' , 'description']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}

    class meta:
        model = product

class productImages(admin.ModelAdmin):
    #readonly_fields = ['image']
    list_display = ['Product','updated']

    class meta:
        model = productImage
#admin.site.register(productSerializers)
admin.site.register(product, productamdin)
admin.site.register(productImage, productImages)
