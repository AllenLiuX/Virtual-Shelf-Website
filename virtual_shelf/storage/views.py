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

def storage_detail(request, id):
    # 取出相应的文章
    storage = StoragePost.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'storage': storage }
    # 载入模板，并返回context对象
    return render(request, 'storage/detail.html', context)

def storage_search(request):
    storages = StoragePost.objects.all()
    context = {'storages': storages}
    return render(request, 'storage/search.html', context)