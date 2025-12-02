from django.urls import path

from new_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dashboard/', views.get, name='dashboard'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path("delete_data/<int:id>",views.delete_data,name="delete_data"),
    path('update_data/<int:id>',views.update_data,name="update_data"),
]