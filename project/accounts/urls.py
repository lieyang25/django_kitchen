from django.urls import path
from .views import register_view, login_view, logout_view
from . import views

app_name = 'accounts'  # 设置命名空间

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #新加入的
    path('page/',views.page,name='page'),
    path('pizzas/',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>',views.pizza,name='pizza')
]
