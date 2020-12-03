from django.urls import path
from .views import home_view, product_list_view, product_create_view, product_delete_view, product_update_view

urlpatterns = [
    path('', home_view, name='products-list'),
    path('products/', product_list_view, name='products-list'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/<int:product_id>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:product_id>/update/', product_update_view, name='product-update')
]
