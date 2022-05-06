from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('menu',views.menu, name='menu'),
    path('menu/<int:pizza_id>/',views.pizza, name='pizza'),
    path('picture', views.pizza, name = 'picture'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)