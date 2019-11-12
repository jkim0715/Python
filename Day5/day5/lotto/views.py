from django.shortcuts import render
import random
from bs4 import BeautifulSoup
import requests
# Create your views here.


def lotto(request):

    return render(request, 'lotto.html')

def winning(request):
    # 1 ~ 45 
    num_list = list(range(46))
    num_count = request.GET['count']
    result = random.sample(num_list, int(num_count))
    result.sort()

    #parsing lotto site
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
    response = requests.get(url)
    html = BeautifulSoup(response.text,'html.parser')
    winning_numbers = html.select('div.win span')
    winning_list = []
    winning_count = 0
    for number in winning_numbers:
        winning_list.append(int(number.text))
        if int(number.text) in result:
            winning_count += 1
            

    return render(request, 'winning.html', {'result' : result,'winning_count':winning_count, 'winning_list':winning_list})


