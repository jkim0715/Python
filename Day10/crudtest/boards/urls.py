from django.contrib import admin
from django.urls import path
from . import views

# URL NameSpace
app_name = 'boards'

urlpatterns = [
    # CRUD 
    ##Request Method에 따라 함수 분리 예정.
    path('', views.index, name = 'index'),
    path('/new/', views.new, name = 'new'),
    #path('/create/', views.create, name = 'create'),
    path('/<int:id>/', views.show, name ='show'),
    path('/<int:id>/edit', views.edit, name = 'edit'),
    #path('/<int:id>/update', views.update, name = "update"),
    path('/<int:id>/delete', views.delete, name = "delete"),
   
]