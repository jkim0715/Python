from django.shortcuts import render
import json
import requests
# Create your views here.


def search(request):
    return render(request, 'search.html')

def result(request):
    keyword = request.GET['search_keyword']

    start_date = request.GET['search_start_date']
    end_date = request.GET['search_end_date']
    time_unit = request.GET['search_time_unit']
    group_name = request.GET['search_group_name']
    keyword = request.GET['search_keyword'].split(',')

    query ={
        "startDate": start_date,
        "endDate": end_date,
        "timeUnit": time_unit,
        "keywordGroups": [
            {
            "groupName": group_name,
            "keywords": keyword
            }
        ]
    }
    url = 'https://openapi.naver.com/v1/datalab/search'
    client_id =''
    client_secret = ''

    headers = {
        'X-Naver-Client-Id' : client_id,
        'X-Naver-Client-Secret' : client_secret
    }

    params = json.dumps(query)
    response = requests.post(url, data=params, headers = headers)
    result = response.text

    context = {
        'result' : result 
    }

    # context = {
    #     'result' : {
    #         'start_date' : start_date,
    #         'end_date' : end_date,
    #         'time_unit' : time_unit,
    #         'group_name' : group_name,
    #         'keyword' : keyword
    #     }   
    # }

    return render(request, 'result.html', context)

