from django import forms
# from django.db import models 

from .models import Article, Comment

## 여기서 Model에 대한 검증을 다한다고 보면됨.. 
## 여기 뚤리면 Model은 다 뚫리는 거로 봄 

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, strip=True)
    email = forms.EmailField()
    class Meta:
        model = Article
        # fields에 all이면 class안에 모든것에 대하여 form적용.
        #fields = '__all__'
        ## 원하는 field만 적용
        #fields = ('title','content')  => 튜플형식
        exclude = ['date']
    # 원래는 이렇게 class랑 똑같이 써놔야 함.
    # title = 
    # content = 
    # email =
    # keyword =
    # date = 
