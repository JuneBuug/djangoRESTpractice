from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from rest_framework import serializers,mixins
from rest_framework.generics import GenericAPIView


def product_page(request):
    return HttpResponse('준')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','img_url','brand','category','data')

class product_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name',None)
        if name is not None :
            queryset = queryset.filter(name=name)
        return queryset