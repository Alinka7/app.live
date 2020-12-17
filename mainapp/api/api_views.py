from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	ListCreateAPIView
	)

from rest_framework.filters import SearchFilter
from .serializers import TagSerializers, ProductSerializers, CustomerSerializers, OrderSerializers
from ..models import Tag, Product, Customer, Order



class TagListCreateApiView(ListAPIView):

	serializer_class = TagSerializers
	queryset = Tag.objects.all()

class ProductListApiView(ListAPIView):
	serializer_class = ProductSerializers
	queryset = Product.objects.all()
	filter_backends = [SearchFilter]
	search_fields = ['price', 'category']


class CustomerListApiView(ListAPIView):
	serializer_class = CustomerSerializers
	queryset = Customer.objects.all()

class OrderListApiView(ListAPIView):
	serializer_class = OrderSerializers
	queryset = Order.objects.all()