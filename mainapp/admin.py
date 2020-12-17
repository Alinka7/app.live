from django.contrib import admin

# Register your models here.

from .models import Customer, Product, Order, Tag



from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'profile_picture', 'date_created')
	list_display_links = ('phone', 'email')
	search_fields = ('name', 'phone')
	list_editable = ('name',)
	list_filter = ('date_created',)


