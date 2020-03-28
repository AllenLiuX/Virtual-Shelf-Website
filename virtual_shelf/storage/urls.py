from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    path('storage-detail/<int:id>/', views.storage_detail, name='storage_detail'),
    path('storage-search/', views.storage_search, name='storage_search'),
    path('storage-list/', views.storage_list, name='storage_list'),
    path('storage-item/<str:item_name>/', views.search_item, name='search_item'),
    path('storage-store/<str:store_name>/', views.search_store, name='search_store'),
    
]