from django.shortcuts import render
from django.http import HttpResponse
from .models import StoragePost, Item, Ownership, Store

def storage_list(request):
    # list out all stores
    # storages = StoragePost.objects.all()
    # # 需要传递给模板（templates）的对象
    # context = { 'storages': storages }
    # # render函数：载入模板，并返回context对象
    ownerships = Ownership.objects.all()
    context = {'ownerships': ownerships}
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

def search_item(request, item_name):
    try:
        item = Item.objects.get(name=item_name)
    except Item.DoesNotExist:
        item = None
    if not item:
        return
    ownerships = Ownership.objects.filter(item=item)
    context = { 'ownerships': ownerships }
    return render(request, 'storage/item_result.html', context)

def search_store(request, store_name):
    try:
        store = Store.objects.get(name=store_name)
    except Store.DoesNotExist:
        store = None
    if not store:
        return 
    ownerships = Ownership.objects.filter(store=store)
    context = { 'ownerships': ownerships }
    return render(request, 'storage/list.html', context)

def search_item_store(request, item_name, store_name):
    try:
        store = Store.objects.get(name=store_name)
    except Store.DoesNotExist:
        store = None
    if not store:
        return 
    try:
        item = Item.objects.get(name=item_name)
    except Item.DoesNotExist:
        item = None
    if not item:
        return 
    ownerships = Ownership.objects.filter(item=item, store=store)
    context = { 'ownerships': ownerships }
    return render(request, 'storage/item_store_result.html', context)