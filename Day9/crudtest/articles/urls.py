from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = "index"),
    path('new/', views.new, name = "new"),
    path('<int:id>/show', views.show, name = "show"),
    path('create/', views.create, name = "create"),
    path('<int:id>/edit/', views.edit, name = "edit"),
    path('<int:id>/update/', views.update, name = "update"),
    path('<int:id>/delete/', views.delete, name = "delete"),  
]