from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Article, Comment, ArticleImages, Board
import json

# Create your views here.

def index(request):
    if request.method=='POST':
        article=Article()
        article.contents=request.POST['contents']
        # 이미지를 받을 때
        # article.image =request.FILES["image"]
        #이미지 리사이즈 
        # article.image_resized = request.FILES["image"]
        article.save()
        for image in request.FILES.getlist('image'):
            ArticleImages.objects.create(article_id=article.id, image=image)
        return redirect('jae:articles')
    else:
        articles = Article.objects.all().order_by("-created_date")
    
        context = {
            'articles' : articles ,
          
        }
    return render(request, 'index.html', context)

def edit(request, article_id):
    article = Article.objects.get(id = article_id)
    if request.method =="POST":
        article.contents = request.POST['contents']
        return redirect("jae:articles")
    else:
        context ={
            'article' :article
        }
        return render(request, 'article/edit.html', context)

def delete(request, article_id):
    article = Article.objects.get(id = article_id)
    article.delete()
    return redirect('jae:articles')

def comments(request):
    if request.method=="POST":
        contents = request.POST["contents"]
        article_id= request.POST["article_id"]
        comment = Comment()
        comment.contents = contents
        comment.article_id= article_id
        comment.save()
        return redirect('jae:articles')
    return ''

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id= comment_id)
    comment.delete()
    return redirect('jae:articles')
    
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id= comment_id)
    if request.method == "POST":
        comment.contents = request.POST['contents']
        comment.save()
        return redirect('jae:articles')
    else:
        context = {
            'comment' : comment
        }
        return render(request, 'comment/edit.html', context)

def js_test(request):
    return render(request, 'js_test.html')

def jq_test(request):
    boards = Board.objects.all().order_by('created_date').reverse()
    context = {
        'boards' :boards
    }
    return render(request, 'jq_test.html', context)

def submit_boards(request):
    if request.method == "POST":
        contents = request.POST["board"]
        board = Board.objects.create(contents=contents)
        context ={
            'board' : board
        }
    return render(request, 'empty.html', context)


def delete_boards(request):
    if request.method  =='POST':
        id = request.POST['board_id']
        board= Board.objects.get(id=id)
        board.delete()
        context = {
            'board_id':id
        }
    return HttpResponse(json.dumps(context), content_type="application/json")

def edit_boards(request):
    if request.method =='POST':
        id =request.POST['board_id']
        contents = request.POST['contents']
        board = Board.objects.get(id=id)
        board.contents = contents
        board.save()
    return HttpResponse('', status = 204)

def edit_comment(request):
    if request.method =='POST':
        id =request.POST['comment_id']
        contents = request.POST['contents']
        comment = Comment.objects.get(id=id)
        comment.contents = contents
        comment.save()
    return HttpResponse('', status = 204)

def delete_comment(request):
    if request.method  =='POST':
        id = request.POST['comment_id']
        comment= Comment.objects.get(id=id)
        comment.delete()
        context = {
            'comment_id':id
        }
    return HttpResponse(json.dumps(context), content_type="application/json")

def submit_comment(request):
    if request.method == "POST":
        contents = request.POST["comment"]
        article_id = request.POST["article_id"]
        comment =Comment.objects.create(contents=contents, article_id=article_id)
        article = Article.objects.get(id=article_id)
        context ={
            'comment' : comment,
            'article' : article
        }
    return render(request, 'comment.html', context)