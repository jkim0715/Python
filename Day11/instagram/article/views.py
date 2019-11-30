from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Article, Comment, ArticleImages, Board, HashTag
import json

# Create your views here.

def index(request):
    if request.method=='POST':

        if request.user.is_authenticated:
            article=Article()
            article.contents=request.POST['contents']
            article.user_id = request.user.id
            article.save()

            tags = request.POST['hashtag']
            for tag in tags.split(","):
                tag = tag.strip()
                if not HashTag.objects.filter(tag= tag):
                    tag = HashTag.objects.create(tag=tag)
                else:
                    tag = HashTag.objects.filter(tag=tag)[0]
                article.tags.add(tag)

        # 이미지를 받을 때
        # article.image =request.FILES["image"]
        #이미지 리사이즈 
        # article.image_resized = request.FILES["image"]
            for image in request.FILES.getlist('image'):
                ArticleImages.objects.create(article_id=article.id, image=image)
            return redirect('jae:articles')
        else:
            return redirect('accounts:login')
    else:
        # ##해시태그를 눌렀을 때 
        # query = request.GET['tags']
        # articles = HashTag.objects.filter(tag=query)[0]

        articles = Article.objects.all().order_by("-created_date")
    
        context = {
            'articles' : articles 
          
        }
    return render(request, 'index.html', context)

def edit(request, article_id):
    article = Article.objects.get(id = article_id)
    if article.is_permitted(request.user.id):
        if request.method =="POST":
            article.contents = request.POST['contents']
            return redirect("jae:articles")
        else:
            context ={
                'article' :article
            }
            return render(request, 'article/edit.html', context)
    else:
        return redirect('jae:articles')
def delete(request, article_id):
    article = Article.objects.get(id = article_id)
    if article.is_permitted(request.user.id):
        article.delete()
        return redirect('jae:articles')
    else:
        return redirect('jae:articles')

def comments(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            contents = request.POST["contents"]
            article_id= request.POST["article_id"]
            comment = Comment()
            comment.contents = contents
            comment.article_id= article_id
            comment.user_id = request.user.id 
            comment.save()
            return redirect('jae:articles')
        else:
            return redirect('accounts:login')
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
        if comment.user_id != request.user.id:
            return HttpResponse('', status =401)
        else:
            comment.contents = contents
            comment.save()
    return HttpResponse('', status = 204)

def delete_comment(request):
    if request.method  =='POST':
        id = request.POST['comment_id']
        comment= Comment.objects.get(id=id)
        if comment.user_id == request.user.id:
            comment.delete()
            context = {
                'comment_id':id
            }
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            return HttpResponse('', status=401)

def submit_comment(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            contents = request.POST["comment"]
            article_id = request.POST["article_id"]
            user_id = request.user.id
            comment =Comment.objects.create(contents=contents, article_id=article_id, user_id=user_id)
            article = Article.objects.get(id=article_id)
            context ={
                'comment' : comment,
                'article' : article,
                # 'username' : comment.user.username,
                # 'comment_id': comment.id,
                # 'article_id' : article.id
            }
            return render(request, 'comment.html', context)
        else:
            context ={
                'status':401,
                'message' : '로그인이 필요합니다.'
            }
            return HttpResponse(json.dumps(context), status =401, content_type = "application/json")


def likes(request):
    if request.user.is_authenticated and request.method == "POST":
        article_id = request.POST['article_id']
        article = Article.objects.get(id= article_id)
        if request.user in article.user_likes.all():
            article.user_likes.remove(request.user) #좋아요 취소
        else:
            article.user_likes.add(request.user) #좋아요
        likes_count = len(article.user_likes.all())
        ##join 을활용해서 배열 순회하면서 좋아요 누른사람들 스트링으로 다떄려박고 합치기
        context = {
            'count': likes_count
        }
        return render(request, 'comment.html', context)
    else:
             
        return HttpResponse('', status = 403)
    