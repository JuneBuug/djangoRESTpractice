from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


# 편리해 앱 모델 만들기
# Product, Review, User 등 간단한 RDB로 구성



class Product(models.Model) :
    name = models.CharField(max_length=256)  # 상품이름
    img_url = models.CharField(max_length=2048)  # 상품 이미지 url
    brand = models.CharField(max_length=128)  # 브랜드 이름
    category = models.CharField(max_length=128)  # 카테고리이름
    price = models.IntegerField  # 가격
    data = JSONField()  # event 정보, flavor_level, grade_avg, grade_count, grade_total, price_level, quantity_level



class Review(models.Model) :
    product = models.ForeignKey(Product)
    comment = models.TextField  # 리뷰 내용
    flavor_score = models.IntegerField  # 맛에 대한 평가 (1~5)
    quantity_score = models.IntegerField  # 양에 대한 평가 (1~5)
    price_score = models.IntegerField  # 가격에 대한 평가 (1~5)
    img_url = models.CharField(max_length=2048)  # 리뷰 이미지 url
    post_date = models.DateTimeField(auto_created=True,auto_now=True)
    useful = models.IntegerField  # 이 리뷰가 유용한지
    bad = models.IntegerField  # 이 리뷰가 별로인지
    # 유저도 foreign key로 추가해야함