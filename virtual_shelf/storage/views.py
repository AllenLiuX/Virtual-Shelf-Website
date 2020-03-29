from django.shortcuts import render
from django.http import HttpResponse
from .models import StoragePost, Item, Ownership, Store
import json

def storage_list(request):
    # list out all stores
    # storages = StoragePost.objects.all()
    # # 需要传递给模板（templates）的对象
    # context = { 'storages': storages }
    # # render函数：载入模板，并返回context对象
    stores = Store.objects.all()
    data = {}
    for s in stores:
        data[s] = Ownership.objects.filter(store=s)
    context = {'data': data}
    return render(request, 'storage/list.html', context)

def storage_detail(request, id):
    # 取出相应的文章
    storage = StoragePost.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'storage': storage }
    # 载入模板，并返回context对象
    return render(request, 'storage/detail.html', context)

def storage_search(request):
    store_list = []
    userId = 1
    for store in Store.objects.all():
        temp = {"userId": userId, "word": store.name, "description": "0"}
        store_list.append(temp)
        userId+=1
    d = {"value": store_list}
    with open('static/suggest/data.json', 'w') as outfile:
        json.dump(d, outfile)

    item_list = []
    userId = 1
    for item in Item.objects.all():
        temp = {"userId": userId, "word": item.name, "description": "0"}
        item_list.append(temp)
        userId+=1
    d = {"value": item_list}
    with open('static/suggest/data2.json', 'w') as outfile:
        json.dump(d, outfile)
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
        store = Store.objects.filter(name=store_name)
    except Store.DoesNotExist:
        store = None
    if not store:
        return 
    data={}
    for s in store:
        ownerships = Ownership.objects.filter(store=s)
        data[s] = ownerships
    context = { 'data': data }
    return render(request, 'storage/store_result.html', context)

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
    return render(request, 'storage/list.html', context)