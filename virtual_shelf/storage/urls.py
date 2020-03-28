from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    path('storage-list/', views.storage_list, name='storage_list'),
    path('storage-detail/<int:id>/', views.storage_detail, name='storage_detail'),
]