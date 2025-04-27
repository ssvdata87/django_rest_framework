from django.urls import path
from .views import *



urlpatterns = [

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:ID>/', ProductDetailViewbyID.as_view(), name='product-detail'),
    path('products/<int:ID>/delete/', DeleteProductbyID.as_view(), name='product-delete'),
    path('products/<int:ID>/update/', UpdateProductbyID.as_view(), name='product-update')
]
