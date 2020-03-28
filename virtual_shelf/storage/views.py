from django.shortcuts import render
from django.http import HttpResponse
from .models import StoragePost

def storage_list(request):
    # 取出所有博客文章
    storages = StoragePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'storages': storages }
    # render函数：载入模板，并返回context对象
    return render(request, 'storage/list.html', context)