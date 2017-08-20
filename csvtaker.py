# -*- conding: utf-8 -*-
import csv
import codecs
from cs.models import Product


with codecs.open('data5.csv', 'r', encoding='utf-8') as csvfile:
     spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         # print(row)
         Product.objects.create(name=row["name"],img_url=row["img"],brand=row["brand"],category=row["category"],data={ "event" : row["event"]})
         # print(row["name"])

