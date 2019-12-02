from django.shortcuts import render, redirect
from django.http.response import HttpResponse 
from .models import Room, Message
import secrets
import json
import pusher


pusher_client = pusher.Pusher(

  app_id='app_id',

  key='app key',

  secret='secret',

  cluster='ap3',

  ssl=True

)


# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['room-title']
        max_count = request.POST['room-max-count']
        code = secrets.token_urlsafe(16)
        room = Room()
        room.title = title
        room.max_connection = max_count
        room.code = code
        room.master_id = request.user.id
        room.save()
        room.users.add(request.user)
        current_connection = len(room.users.all())

        context ={
            'id':room.id,
            'title':title,
            'max_connection': max_count,
            'current_connection': current_connection,
            'master' : room.master.username
        }   
        pusher_client.trigger('main', 'create-room', json.dumps(context))
   
        return HttpResponse('', status = 204)
    else:
        rooms = Room.objects.all()
        context={
            'rooms' : rooms
        }
        return render(request, 'index.html', context)

def show(request, room_id):
    if request.user.is_authenticated:
        room = Room.objects.get(id=room_id)
        room.users.add(request.user)
        join_message = {
            'user': request.user.username,
            'contents': f'{request.user.username}님이 방에 들어왔습니다.'
        }
        pusher_client.trigger(room.code, 'chat', json.dumps(join_message))
        messages = Message.objects.filter(room_id=room.id).order_by("created_at")
        context = {
            'room_id': room_id,
            'current_connection': len(room.users.all())
        }
        pusher_client.trigger('main', 'update-room', json.dumps(context))

        context2 = {
            'room': room,
            'messages': messages
        }
        return render(request, 'show.html', context2)
    else:
        return redirect('account:login')


def chat(request, room_id):
    room = Room.objects.get(id=room_id)
    message = Message()
    message.room_id = room.id
    message.contents = request.POST['contents']
    message.user_id = request.user.id 
    message.save()

    context ={
        'contents': message.contents,
        'user' : request.user.username
    }
    ## 메인에서 대화내용 보지도 않을건데 굳이 채널을 main이랑 같이 쓸 필요 없음
    pusher_client.trigger(room.code, 'chat', json.dumps(context))
    return HttpResponse('', status =204 )


def exit(request, room_id):
    room = Room.objects.get(id=room_id)
    room.users.remove(request.user)
    join_message = {
            'user': request.user.username,
            'contents': f'{request.user.username}님이 방에서 나갔습니다.'
        }
    pusher_client.trigger(room.code, 'chat', json.dumps(join_message))
    context = {
        'room_id': room_id,
        'current_connection': len(room.users.all())
    }
    pusher_client.trigger('main', 'update-room', json.dumps(context))
    return redirect('boards:index')
