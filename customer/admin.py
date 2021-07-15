from django.contrib import admin
from .models import MenuItem, Category, OrderModel, Quantity
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(Quantity)