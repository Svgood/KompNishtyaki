from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goods/', views.goods, name='goods'),
    path('goods/<int:good_id>', views.good, name='good'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]