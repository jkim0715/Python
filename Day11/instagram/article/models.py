from django.db import models 
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail
# Create your models here.
class Article(models.Model):
    contents = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
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
        return Comment.objects.filter(article_id=self.id)
        
    def article_images(self):
        return ArticleImages.objects.filter(article_id=self.id)

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


class Board(models.Model):
    contents = models.CharField(max_length =16)
    created_date = models.DateTimeField(auto_now_add= True)