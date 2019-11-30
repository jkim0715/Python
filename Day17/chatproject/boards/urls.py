from django.urls import path
# 현재 폴더에 있는 views.py 파일을 가져온거임.
from . import views 

app_name ='boards'

urlpatterns = [
    path('', views.index, name = 'index'),
    #채팅방 안에 들어간거
    path('<int:room_id>/', views.show, name = 'room'),
    path('<int:room_id>/exit/', views.exit, name="exit"),
    path('<int:room_id>/message/', views.chat, name="chat"),
    
]