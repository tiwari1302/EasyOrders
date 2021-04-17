from django.shortcuts import render
from django.views import View
from .models import Category, MenuItem, OrderModel
# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        sandwiches = MenuItem.objects.filter(category__name__contains='Sandwich')
        pizzas = MenuItem.objects.filter(category__name__contains='Pizza')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # pass into context
        context = {
            'sandwiches': sandwiches,
            'pizzas': pizzas,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])
        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email
        )
        order.items.add(*item_ids)

        context = {
        'items': order_items['items'],
        'price': price
        }

        return render(request, 'customer/order_confirmation.html', context)