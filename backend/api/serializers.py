from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price']

    @staticmethod
    def validate_price(value):
        if value < 0:
            raise serializers.ValidationError(
                'Цена должна быть положительным числом.'
            )
        return value

    def validate(self, data):
        if 'title' in data and len(data['title']) < 1:
            raise serializers.ValidationError(
                'Длина заголовка должна составлять не менее 1 символа.'
            )
        return data
