from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StoragePost, Item, Ownership, Store
from .forms import StoragePostForm
from django.contrib.auth.models import User
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

def storage_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        storage_post_form = StoragePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if storage_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_storage = storage_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_storage.store = Store.objects.get(name=new_storage.storename)
            new_storage.item = Item.objects.get(name=new_storage.itemname)
            # 将新文章保存到数据库中
            new_storage.save()
            # 完成后返回到文章列表
            return redirect("storage:storage_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        storage_post_form = StoragePostForm()
        # 赋值上下文
        context = { 'storage_post_form': storage_post_form }
        # 返回模板
        return render(request, 'storage/create.html', context)