from django.contrib import admin

# Register your models here.
from django.contrib import admin

# 别忘了导入ArticlerPost
from .models import StoragePost

from .models import Item

from .models import Store

from .models import Ownership

# 注册ArticlePost到admin中
admin.site.register(StoragePost)

admin.site.register(Item)

admin.site.register(Store)

admin.site.register(Ownership)