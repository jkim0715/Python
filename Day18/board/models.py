from django.db import models

from faker import Faker
f = Faker()
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=300)
    keyword = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True, null=True)

    @classmethod
    def dummy(cls, n):
        # cls는 
        # article = clas();
        # article.title ="asdf"s
        # ...
        # article.save()
        for i in range(n):
            cls.objects.create(
                title = f.text(20),
                content=f.text(),
                keyword=f.company(),
                email=f.email(),
            )
    

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)