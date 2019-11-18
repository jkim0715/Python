from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=16)
    contents= models.TextField()
    creator = models.CharField(max_length=8)
    created_date = models.DateTimeField(auto_now_add=True, null =True)
    updated_date = models.DateTimeField(auto_now=True, null = True)

    def __str__(self):
        return f'[Title : {self.title} Created By {self.creator} - {self.created_date.strftime("%Y-%m-%d")}]'

    def datetime_to_string(self):

        return self.created_date.strftime("%Y-%m-%d")


    def created_by(self):
        return "Created By:" + self.creator