from django.shortcuts import render
import requests 
import json
# Create your views here.



def main(request):
    return render(request, 'kakao_main.html')

def find_address(request):
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    key = ''
    q = request.GET['address']
   
    params ={
        'query' : q,
        'size'  : 30
    }

    headers = {
        'Authorization' : f'KakaoAK {key}'
    }
    ## url 요청할때 .json으로 요청했기 때문에 response의 type은 JSON임.
    response = requests.get(url, params=params, headers=headers)
    
    ##json으로 요청했는데 str로 날라옴.. 그래서 강제로 json.loads로 dictionary로 바꿔버림
    address_data = json.loads(response.text)

    context ={
        'data' : address_data["documents"]
    }


    return render(request, 'kakao_find_address.html', context)

def keyword_result(request):
    # 키워드를 입력하는 곳에서 입력한 키워드
    # position (위도,경도) 좌표를 추출해서 
    # kakao api의 키워드 검색 api에 요청
    keyword = request.GET['keyword']
    position = request.GET['position']
    gps_x = position.split(',')[0]
    gps_y = position.split(',')[1]

    url ='https://dapi.kakao.com/v2/local/search/keyword.json'
    key = ''
    params = {
        'query' :keyword,
        'x': gps_x,
        'y': gps_y
    }
    
    headers ={
        'Authorization': f'KakaoAK {key}'
    }

    response = requests.get(url, params= params, headers = headers)
    context = {
        'result' : json.loads(response.text)["documents"]
    }
    
    return render(request, 'keyword_result.html', context)