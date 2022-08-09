from django.contrib import admin
from django.urls import path, include
from products.views import list_products, create_product, update_product, delete_product, primer_formulario, search_products

urlpatterns = [
    path("list_products/",list_products,name="list_products"),
    path("create_product/",create_product,name="create_product"),
    path("primer_formulario/",primer_formulario,name="primer_formulario"),
    path("search_products/",search_products,name="search_products"),
    path("delete_product/<int:pk>/" ,delete_product, name="delete_product"),
    path("update_product/<int:pk>/",update_product, name="update_product")
]