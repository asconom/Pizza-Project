from django.shortcuts import render, redirect
from .forms import CommentForm
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
    toppings = pizza.toppings_set.all()
    comment = pizza.comment_set.all()
    
    context = {'pizza':pizza, 'toppings':toppings, 'comment':comment} 

    return render(request, 'pizzas/pizza.html', context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza} 
    return render(request, 'pizzas/new_comment.html', context)

