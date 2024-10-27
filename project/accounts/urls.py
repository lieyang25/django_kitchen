from django.urls import path
from .views import register_view, login_view, logout_view
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    #新加入的
    path('page/',views.page,name='page'),
    path('pizzas/',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>',views.pizza,name='pizza')
]
