from rest_framework import serializers
from ..models import Tag, Product, Customer, Order

class TagSerializers(serializers.ModelSerializer):
	name = serializers.CharField(required=True)

	class Meta:
		model = Tag
		fields =['id', 'name']

class ProductSerializers(serializers.ModelSerializer):

	name = serializers.CharField(required=True)
	price = serializers.FloatField(required=True)
	category = serializers.CharField(required=True)
	description = serializers.CharField(required=True)
	date_created = serializers.DateTimeField(required=True)
	tags = serializers.StringRelatedField(many=True)
	class Meta:
		model = Product
		fields = '__all__'

class CustomerSerializers(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
	customer = CustomerSerializers(required=True)
	product = ProductSerializers(required=True)
	class Meta:
		model = Order
		fields = '__all__'