from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    path('storage-list/', views.storage_list, name='storage_list'),
]