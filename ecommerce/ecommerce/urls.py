"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from products.views import home, detail, search, listproductAPI
from cart.views import view, cart_update
from order.views import checkout, Orders
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', home, name='home'),
    
    url(r'^api/', listproductAPI.as_view(), name='productAPI'),
    url(r'^cart/(?P<slug>[\w-]+)/$', cart_update, name='cart_update'),
    url(r'^cart/', view, name='view'),
    url(r'^s/$', search, name='searchproduct'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^orders/$', Orders, name='orders'),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='details'),
    
    
        
]

urlpatterns = format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
