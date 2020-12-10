from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import home_view, product_list_view, product_create_view, product_delete_view, product_update_view
from .views_function import product_list, product_detail
from .views_class import ProductAPIView, ProductDetailsAPIView
from .views_generic import ProductList, ProductDetail
from .views_router import ProductViewSet


# urlpatterns = [
#     path('', home_view, name='home'),
#     path('products/', product_list_view, name='products-list'),
#     path('products/create/', product_create_view, name='product-create'),
#     path('products/<int:product_id>/delete/', product_delete_view, name='product-delete'),
#     path('products/<int:product_id>/update/', product_update_view, name='product-update')
# ]

# urlpatterns = [
#     path('products/', product_list, name='products'),
#     path('products/<int:pk>/', product_detail, name='product-details'),
# ]

# urlpatterns = [
#     path('products/', ProductAPIView.as_view(), name='products'),
#     path('products/<int:pk>/', ProductDetailsAPIView.as_view(), name='product-details'),
# ]

# urlpatterns = [
#     path('products/', ProductList.as_view(), name='products'),
#     path('products/<int:pk>/', ProductDetail.as_view(), name='product-details'),
# ]

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = router.urls
