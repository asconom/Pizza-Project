from django.shortcuts import render
from .models import Pizza, Toppings
# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def menu(request):
    menu = Pizza.objects.all()

    context = {'menu':menu}

    return render(request, 'pizzas/menu.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    picture = Pizza.picture
    toppings = pizza.toppings_set.all()
    
    context = {'pizza':pizza, 'picture':picture, 'toppings':toppings} 

    return render(request, 'pizzas/pizza.html', context)
