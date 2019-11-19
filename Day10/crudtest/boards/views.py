from django.shortcuts import render, redirect

from .models import Board
# Create your views here.


def index(request):
    ##객체 리스트 뿌려주기
    boards = Board.objects.all()
    context = {
        'boards' : boards
    }
    return render(request, 'index.html', context)

def new(request):
    #new 
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        author = request.POST['author']

        board = Board.objects.create(title = title, contents = contents, author = author )
        return redirect('boards:show', board.id)
    return render(request, 'new.html')

#Create는 view가 따로 없음
## Request Method에 따라 함수 merge
'''
def create(request):
    title = request.GET['title']
    contents = request.GET['contents']
    author = request.GET['author']

    board = Board.objects.create(title = title, contents = contents, author = author )
    return redirect('boards:show', board.id)

'''


def show(request, id):
    board = Board.objects.get(id= id)
    context = {
        'board' : board
    }
    return render(request, 'show.html', context)

def edit(request, id):
    if request.method == 'POST':
        board = Board.objects.get(id= id)
        title = request.POST['title']
        contents = request.POST['contents']
        author = request.POST['author']

        board.title = title
        board.contents = contents
        board.author = author
        board.save()

        context = {
            'board' : board
        }

        return redirect('boards:show', board.id)
    board = Board.objects.get(id= id)
    context ={
        'board' : board
    }

    return render(request, 'edit.html', context)


'''
##redirect
def update(request, id):
    board = Board.objects.get(id= id)
    title = request.GET['title']
    contents = request.GET['contents']
    author = request.GET['author']

    board.title = title
    board.contents = contents
    board.author = author
    board.save()

    context = {
        'board' : board
    }

    return redirect('boards:show', board.id)
'''



def delete(request, id):
    board = Board.objects.get(id= id)
    board.delete()
    
    return redirect('boards:index')
