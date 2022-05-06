from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('menu',views.menu, name='menu'),
    path('menu/<int:pizza_id>/',views.pizza, name='pizza')
]

urlpatterns += staticfiles_urlpatterns()