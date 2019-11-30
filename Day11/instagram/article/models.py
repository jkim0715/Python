from django.db import models 
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    contents = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="article_likes")


    #image = models.ImageField(blank = True)

    # image_resized = ProcessedImageField(
    #     #source='image', 이건 imagespecfield에 있는건데 이따 썸네일 할때 쓸 거임
    #     upload_to='article/images',
    #     processors=[ResizeToFill(200,200)],
    #     format='JPEG',
    #     options={'quality':90}
    # )

    #이미지의 썸네일을 생성해줌
    # media/CACHE에 원본 이미지의 썸네일을 자동 생성
    # image_thumbnail =ImageSpecField(
    #     source='image',
    #     processors=[Thumbnail(200,200)],
    #     format='JPEG',
    #     options={'quality':90}


    # )

    def comments(self):
        return Comment.objects.filter(article_id=self.id).order_by('created_date').reverse()
        
    def article_images(self):
        return ArticleImages.objects.filter(article_id=self.id)

    # 글을 작성한 아이디와, Target아이디(현재로그인한 아이디)가 같은지 판별하는 Model funciton
    def is_permitted(self, target_id):
        return self.user_id == target_id

class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(300,300)],
        format='JPEG',
        options={'quality':90}
    )
    




class Comment(models.Model):
    contents = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





class Board(models.Model):
    contents = models.CharField(max_length =16)
    created_date = models.DateTimeField(auto_now_add= True)



class HashTag(models.Model):
    tag = models.CharField(max_length = 16, unique= True)
    articles = models.ManyToManyField(Article, related_name="tags")