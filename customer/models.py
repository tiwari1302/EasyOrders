from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(MenuItem, related_name='order', blank=True, through='Quantity')
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        item_list = dict()
        
        m = Quantity.objects.filter(order=self)
        for each in m:
            item_list[each.item.name] = each.count
        
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")} - Items= {item_list} '

class Quantity(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(null=False, default=1)
