from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.product_create, name='create-product'),
    path('list/', views.list_products, name='list-products'),
    path('get/<int:product_id>/', views.get_product, name='get-product'),
    path('update/<int:product_id>/', views.update_product, name='update-product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete-product'),
]
