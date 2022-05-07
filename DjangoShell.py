import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")
from PIL import Image

import django
django.setup()

from pizzas.models import Pizza, Comment

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, '  ', p)

p = Pizza.objects.get(id=1)

print(p.pizza_name)

toppings = p.toppings_set.all()

for t in toppings:
    print(t.topping_name)

for p in pizzas:
    print(p)
    im = Image.open(p.picture)
    im.show()
    for t in toppings:
        print(t.topping_name)
        
