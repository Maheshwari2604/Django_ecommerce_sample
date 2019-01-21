from rest_framework import serializers
from .models import product, productImage


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        #fields = ('title', 'description', 'price')
        fields = '__all__'


class productImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = productImage
        fields = '__all__'
