from django.urls import path

from new_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_todo/', views.add_todo, name='add_todo'),
]