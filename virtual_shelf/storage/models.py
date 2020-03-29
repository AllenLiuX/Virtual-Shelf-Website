from django.db import models
# 导入内建的User模型。
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class StoragePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Item(models.Model):
	category = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Store(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	items = models.ManyToManyField(Item, through='Ownership')

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Ownership(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	itemname = models.CharField(max_length=100, default=item.name)
	storename = models.CharField(max_length=100, default=store.name)
	price = models.FloatField()
	quantity = models.IntegerField()
	created = models.DateTimeField(default=timezone.now)
	#author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(id=1))

	class Meta:
		ordering = ['store']

	def __str__(self):
		return str(self.quantity) + " " + self.item.name + " in " + self.store.name
