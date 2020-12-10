from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = serializers.ALL_FIELDS


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.IntegerField(write_only=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'display_price', 'category', 'price']

    def validate_price(self, price):
        if 0 < price < 100:
            return price
        raise serializers.ValidationError('Price can only be assigned a value between 0 and 100.')


