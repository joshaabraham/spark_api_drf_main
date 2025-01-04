from django.urls import path
from . import views

urlpatterns = [
    path("categoriesCreateList/", views.CategoryListCreateView.as_view(), name="category_list_create"),
    path("categorie/<int:pk>/", views.CategoryRetrieveUpdateDestroyView.as_view(), name="category_detail"),
    path("productsCreateList/", views.ProductListCreateView.as_view(), name="product_list_create"),
    path("product/<int:pk>/", views.ProductRetrieveUpdateDestroyView.as_view(), name="product_detail"),
    path("customersCreateList/", views.CustomerListCreateView.as_view(), name="customer_list_create"),
    path("customer/<int:pk>/", views.CustomerRetrieveUpdateDestroyView.as_view(), name="customer_detail"),
    path("ordersCreateList/", views.OrderListCreateView.as_view(), name="order_list_create"),
    path("order/<int:pk>/", views.OrderRetrieveUpdateDestroyView.as_view(), name="order_detail"),
    path("orderitemsCreateList/", views.OrderItemListCreateView.as_view(), name="orderitem_list_create"),
    path("orderitem/<int:pk>/", views.OrderItemRetrieveUpdateDestroyView.as_view(), name="orderitem_detail"),
]