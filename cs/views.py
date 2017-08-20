from django.db.models import IntegerField
from django.db.models.functions import Cast
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
        fields = ('name','img_url','brand','category','data','price')

class product_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def get_queryset(self):
        queryset = Product.objects.all()

        order = self.request.query_params.get('order', None)
        if order is not None:
            if order == "1":
                queryset = Product.objects.extra(
                    select={'myinteger': "CAST(substring(price FROM '^[0-9]+') AS INTEGER)"}
                ).order_by('myinteger')

        name = self.request.query_params.get('name',None)
        if name is not None :
            queryset = queryset.filter(name=name)

        brand = self.request.query_params.get('brand',None)
        if brand is not None:
            queryset = queryset.filter(brand=brand)

        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)

        # event = self.request.query_params.get('event', None)
        # if event is not None:
        #     queryset = queryset.filter(data__event=event)
        # 왜 안될까

        return queryset