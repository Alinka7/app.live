import django_filters
from django_filters import DateFilter
from .models import * 

class FilterOrder(django_filters.FilterSet):
	start = DateFilter(field_name='date_created', lookup_expr='gte')
	end = DateFilter(field_name='date_created', lookup_expr='lte')
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['date_created', 'customer']