from django.shortcuts import render, redirect
from .models import Boards

# Create your views here.

def index(request):
    #Board 모델에 담긴 모든 글들을 가져와서 보여줌 
    boards = Boards.objects.all()

    context = {
        'boards' : boards
    }

    return render(request,'index.html', context)
def new(request):
    return render(request, 'new.html')


def create(request):
    
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']

    new_board = Boards(title = title, contents = contents, creator = creator)
    #new_board.title = title
    #new_board.contents = contents
    #new_board.creator = creator
    new_board.save()
    #위 두줄을 한줄 로 만드는 방법
    #new_board = Board.objects.create(title = title, contents = contents, creator = creator)

    return redirect(f'/boards/{new_board.id}')

def edit(request,id):
    #원래 있던 내용이 들어있는 form
    board = Boards.objects.get(id=id)    
    context ={
        'board' :board
    }
    return render(request, 'edit.html', context)

def update(request,id):
    #실제로 update가 이뤄지는 곳 
    board = Boards.objects.get(id=id)
    title = request.GET['title']
    contents = request.GET['contents']

    board.title = title
    board.contents = contents
    board.save()
    context = {
        'board' : board
    }


    return redirect(f'/boards/{board.id}')
def show(request, id):
    #파라미터로 넘어오는 값은 모두 str, 하지만 table에 id는 int형이기 때문에 형변환 필요.
    board = Boards.objects.get(id=int(id))

    context = {
        'board' : board
    }
    
    return render(request, 'show.html',context)

def delete(request, id):
    board = Boards.objects.get(id=int(id))
    board.delete()

    return redirect('/boards')