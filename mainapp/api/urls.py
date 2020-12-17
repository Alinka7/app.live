from django.urls import path

from .api_views import(
TagListCreateApiView, 
ProductListApiView, 
CustomerListApiView,
OrderListApiView
)

urlpatterns = [
	path('tags/', TagListCreateApiView.as_view(), name='tags'),
	path('products/', ProductListApiView.as_view(), name='products'),
	path('customers/', CustomerListApiView.as_view(), name='customers'),
	path('orders/', OrderListApiView.as_view(), name='orders')
]
