# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import product, productImage
from django.shortcuts import render, Http404, HttpResponse
from .serializers import productSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
def home(request):
    products = product.objects.all()
    context = {
        'products': products 
    }
    return render(request, 'products/home.html',context)


#API
class listproductAPI(generics.ListAPIView):
    queryset = product.objects.all()
    #productImages = products.productImage_set.all()
    #productImages = productImage.objects.all()
    serializer_class = productSerializer
    #serializer1 = productImageSerializers(productImages, many=True)
    
    # context = {
    #     'serializers': serializer
    #     #"serializer1": serializer1,
    # }
    # return render(request, 'products/apii.html', context)
    #serialize = serializer.encode("acsii","replace")
    #return HttpResponse(serializer.data) 
    #return HttpResponse(serializer1.data)
    


def search(request):
    q = request.GET.get('Keyword')
    #return HttpResponse(q)
    products = product.objects.filter(title__icontains=q)
    #print products
    #return HttpResponse(products)
    if products:
        context = {"products": products, "query": q}
    else:
        message = "Somethings wents wrong! please try something new"
        context = {"empty": True, 'message': message, "query": q}
    return render(request, 'products/result.html', context)


def detail(request, slug):
    #try:
        details = product.objects.get(slug=slug)
        context = {
            'details': details
        }
        return render(request, 'products/detail.html', context)
#except:
    #    raise Http404
