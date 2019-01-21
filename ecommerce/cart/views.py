# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cart, CartItem
from products.models import product
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse

# Create your views here.

def view(request):
    try:
        the_id = request.session['cart_Id']
    except:
        the_id = None
        message = "Please do shoping, you have nothing in your cart"
        context = {"empty": True, "message": message}
        return render(request, 'cart/view.html', context)

    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart}    
    else:
        message = "Please do shoping, you have nothing in your cart"
        context = {"empty": True, "message": message}
    #template = "cart/view.html"
    return render(request, 'cart/view.html', context) 


def cart_update(request, slug):
    #return HttpResponse(slug)
    request.session.set_expiry(300)

    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        the_id = request.session['cart_Id']
    except:
       new_item = Cart()
       new_item.save()
       request.session['cart_Id'] = new_item.id
       the_id = new_item.id

    cart = Cart.objects.get(id=the_id)
    #return render(request, 'cart/result.html', context)
    #print "hello"
    #context = {"cart":cart }
    try:
        prod = product.objects.get(slug=slug)
        #return HttpResponse(products)
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=prod)

#    if not cart_item in cart.item.all():
#        cart.item.add(cart_item)
#    else:
#          cart.item.remove(cart_item)    

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass
  
    new_item = 0.00
    for item in cart.cartitem_set.all():
        totalitem = float(item.product.price) * item.quantity
        new_item += totalitem

    request.session['item_total'] = cart.cartitem_set.count()
    #print cart.products.count()
    cart.Total = new_item
    cart.save()    

    return HttpResponseRedirect(reverse("view"))


'''
    if not prod in cart.products.all():
        cart.products.add(prod)
    else:
        cart.products.remove(prod)  
'''
