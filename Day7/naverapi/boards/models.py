from django.db import models

# Create your models here.

class Board(models.Model):
    # Table 만드는 과정.
    title = models.CharField(max_length=30)
    contents = models.TextField()

    ## 추가부분 
    created_by = models.CharField(max_length=10, null=True)

    