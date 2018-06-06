from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goods/', views.goods, name='goods'),
    path('goods/<int:good_id>', views.good, name='good'),
    path('auth/', views.auth, name='auth'),
    path('reg/', views.reg, name='reg'),
    path('basket/', views.basket, name='basket'),
    path('deleteFromBasket/<int:good_id>', views.deleteFromBasket, name='delete'),
]