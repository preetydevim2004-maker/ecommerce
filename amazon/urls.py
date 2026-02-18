from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),

    path('increase/<int:id>/', views.increase, name='increase'),
    path('decrease/<int:id>/', views.decrease, name='decrease'),
    path('remove/<int:id>/', views.remove, name='remove'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),    
    path('logout/', views.user_logout, name='logout'),   
    path('checkout/', views.checkout, name='checkout'), 
    path('order_success/<int:id>/', views.order_success, name='order_success'), 
    path('order/<int:id>/', views.order_detail, name='order_detail'), 
    
    
    path('api/products/',views.product_api),

]
