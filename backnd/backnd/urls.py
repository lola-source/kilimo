"""backnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    retailer_list,
    retailer_detail,
    retailer_create,
    retailer_update,
    retailer_delete,
    supplier_list,
    supplier_detail,
    supplier_create,
    supplier_update,
    supplier_delete,
    produce_list,
    produce_detail,
    produce_create,
    produce_update,
    produce_delete,
)

urlpatterns = [
    # Fresh Produce Retailer URLs
    path('retailers/', retailer_list, name='retailer_list'),
    path('retailers/<int:retailer_id>/', retailer_detail, name='retailer_detail'),
    path('retailers/create/', retailer_create, name='retailer_create'),
    path('retailers/<int:retailer_id>/update/', retailer_update, name='retailer_update'),
    path('retailers/<int:retailer_id>/delete/', retailer_delete, name='retailer_delete'),

    # Supplier URLs
    path('suppliers/', supplier_list, name='supplier_list'),
    path('suppliers/<int:supplier_id>/', supplier_detail, name='supplier_detail'),
    path('suppliers/create/', supplier_create, name='supplier_create'),
    path('suppliers/<int:supplier_id>/update/', supplier_update, name='supplier_update'),
    path('suppliers/<int:supplier_id>/delete/', supplier_delete, name='supplier_delete'),

    # Fresh Produce URLs
    path('produces/', produce_list, name='produce_list'),
    path('produces/<int:produce_id>/', produce_detail, name='produce_detail'),
    path('produces/create/', produce_create, name='produce_create'),
    path('produces/<int:produce_id>/update/', produce_update, name='produce_update'),
    path('produces/<int:produce_id>/delete/', produce_delete, name='produce_delete'),
]
