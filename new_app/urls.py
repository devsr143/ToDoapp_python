from django.urls import path

from new_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]