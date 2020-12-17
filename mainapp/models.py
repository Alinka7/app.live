from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=True)
	phone = models.CharField(max_length=15, null=True)
	email = models.CharField(max_length=30, null=True)
	profile_picture = models.ImageField(default="anonim.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name or ''



class Tag(models.Model):
	name = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.name or ''



class Product(models.Model):
	CATEGORY = (
		('sport_car', 'sport_car'),
		('car', 'car'),)
	name = models.CharField(max_length=255, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=255, null=True, choices=CATEGORY)
	description = models.CharField(max_length=255, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name or ''


		
class Order(models.Model):
	STATUS = (
		('hanging', 'hanging'),
		('for_delivery', 'for_delivery'),
		)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True,choices=STATUS)
	
	def __str__(self):
		return self.product.name or ''
