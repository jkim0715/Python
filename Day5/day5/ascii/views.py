from django.shortcuts import render
import requests
import json

# Create your views here.

def ascii(request):
    ## 입력하고자 하는 text를 받아야함
    #ascii에서 제공하는 폰트 
    url = 'http://artii.herokuapp.com/fonts_list'
    response = requests.get(url)
    fonts_list = response.text.split('\n')
    context = {
        'fonts' : fonts_list
    }
    return render(request, 'ascii.html', context)

def result(request):
    font = request.GET['font']
    text = request.GET['text']
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    response = requests.get(url)
    context = {
        'result' : response.text
    }
    return render(request, 'result.html', context)