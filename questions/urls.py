from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:either_id>/comments/create/', views.comment_create, name='comment_create'),
    path('random/', views.random, name='random')
]