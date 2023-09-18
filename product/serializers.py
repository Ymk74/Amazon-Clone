from rest_framework import serializers
from .models import Product ,Brand
from django.db.models.aggregates import Avg


class BrandListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
#  brand = BrandListSerializer()
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
#    price_with_tax = serializers.SerializerMethodField()
    class Meta :
        model = Product
        fields = '__all__'

# def get_price_with_tax(self,product):
    #    return product.price*1.5
    
    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg'] :
            result = 0
            return result
        return avg['rate_avg']

    def get_reviews_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews 


class ProductDetailSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    class Meta :
        model = Product
        fields = '__all__'


    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg'] :
            result = 0
            return result
        return avg['rate_avg']

    def get_reviews_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews 




class BrandDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(source='product_brand',many=True)
    class Meta :
        model = Brand
        fields = '__all__'