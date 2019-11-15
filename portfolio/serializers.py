from rest_framework import serializers
from .models import Customer, Investment, Stock


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['cust_number', 'name','address','city','state','zipcode', 'email', 'cell_phone', 'created_date', 'updated_date' ]


class InvestmentSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='customer.name',read_only=True)

    class Meta:
        model = Investment
        fields = '__all__'
        depth = 1


class StockSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='customer.name', read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'
        depth = 1
