  
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.

from .models import *
from .all_forms import FormOrder, CreateUserForm, CustomerForm
from .django_filters import FilterOrder

from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registration(request):
	
	form  = CreateUserForm()
	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user_name = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			Customer.objects.create(
				user = user,
				)

			messages.success(request, 'Account was created for ' + user_name)
			return redirect('login_page')
	context = {'form': form}

	return render(request, 'accounts/register_page.html', context)


@unauthenticated_user
def loginPage(request):
	

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('home_page')
		else:
			messages.info(request, 'username or password is incorrect')

	context = {}
	return render(request, 'accounts/login_page.html', context)


def logoutUser(request):

	logout(request)
	return redirect('login_page')



@login_required(login_url='login_page')
@admin_only
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	all_customers = customers.count()

	all_orders = orders.count()

	for_delivery= orders.filter(status='for_delivery').count()
	hanging = orders.filter(status='hanging').count()

	context = {
		'orders': orders,
		'customers': customers,
		'all_customers': all_customers,
		'all_orders': all_orders,
		'for_delivery': for_delivery,
		'hanging': hanging
		}
	return render(request, 'accounts/dashboard.html', context)




@login_required(login_url='login_page')
@allowed_users(allowed_pople=['customer'])
def userPage(request):
	orders = request.user.customer.order_set.all()
	all_orders = orders.count()

	for_delivery= orders.filter(status='for_delivery').count()
	hanging = orders.filter(status='hanging').count()

	print('orders', orders)
	context={
	'orders': orders,
	'all_orders' : all_orders,
	'for_delivery': for_delivery, 
	'hanging': hanging 
	}
	return render(request, 'accounts/user.html', context)



@login_required(login_url='login_page')
@allowed_users(allowed_pople=['customer'])
def account_settings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		if form.is_valid():
			form.save()

	context={'form': form}
	return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login_page')
@allowed_users(allowed_pople=['admin'])

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products': products})
#primary key

@login_required(login_url='login_page')
@allowed_users(allowed_pople=['admin'])

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	all_orders_count = orders.count()

	customer_filter = FilterOrder(request.GET, queryset=orders)
	orders = customer_filter.qs
	context = {
		'customer': customer,
		'orders': orders,
		'all_orders_count': all_orders_count,
		'customer_filter': customer_filter
	}
	return render(request, 'accounts/customer.html', context)


# @login_required(login_url='login_page')
# @allowed_users(allowed_pople=['admin'])

def create_order(request):
	form = FormOrder()
	if request.method == 'POST':
	# 	print('Printing POST:', request.POST)
		form = FormOrder(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	

	return render(request, 'accounts/order_form.html', context)


# @login_required(login_url='login_page')
# @allowed_users(allowed_pople=['admin'])

def update_order(request, pk):

	order = Order.objects.get(id=pk)
	form = FormOrder(instance=order)
	if request.method == 'POST':

		form=FormOrder(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form': form,
	'order': order}
	return render(request, 'accounts/order_form.html', context)


# @login_required(login_url='login_page')
# @allowed_users(allowed_pople=['admin'])

def delete_order(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
	context={'item': order}
	return render(request, 'accounts/delete.html', context)

	
