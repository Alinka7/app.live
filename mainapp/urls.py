from django.urls import path
from . import views




urlpatterns = [
	path('register_page/', views.registration, name='register_page'),
    path('login_page/', views.loginPage, name='login_page'),
    path('logout_page/', views.logoutUser, name='logout_page'),
    

    path('', views.home, name='home_page'),
    path('user/', views.userPage, name='user_page'),

    path('account/', views.account_settings, name='account'),
    
    path('products/', views.products, name='products_page'),
    path('customer/<str:pk>/', views.customer, name='customer_page'),
    

    path('create_order/', views.create_order, name="create_order"),    
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order')
  

]

