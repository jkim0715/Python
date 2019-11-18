from django.shortcuts import render, redirect
from .models import Article
# Create your views here.


def index(request):
    #여기는처음에 접속하면 article 리스트를 뿌려야겠지요..
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'index.html', context)

def show(request, id):
    #article을 선택 했을 때, id를 받아서 detail을 보여줘야되고
    article = Article.objects.get(id=id)
    context ={
        'article' : article
    }
    return render(request, 'show.html', context)

def new(request):
    #새로운 article 작성 페이지로 이동 
    return render(request, 'new.html')

# view가 필요없는 친구들이 뭔지 생각하고 코딩하기.
def create(request):
    #article을 새로 생성 ('작성하기 버튼 누를 때')
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']
    #1. 
    #article = Article.objects.create(title = title, contents= contents, creator= creator)
    #2.
    article = Article()
    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()
    #1,2 아무거나 사용
    return redirect('articles:show', article.id)

def edit(request, id):
    article = Article.objects.get(id=id)
    context ={
        'article' : article
    }
    return render(request, 'edit.html',context)

def update(request, id):
    article = Article.objects.get(id=id)
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']

    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()

    context ={
        'article' : article
    }
    return redirect('articles:index')

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')
   


