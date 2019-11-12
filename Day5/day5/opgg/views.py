from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def opgg(request):
    return render(request, 'opgg.html')

def result(request):

    user = request.GET['user']
    url = f'https://www.op.gg/summoner/userName={user}'
    response = requests.get(url)
    html = BeautifulSoup(response.text,'html.parser')

    if html.select_one('span.WinLose .wins') is None :
        results = {
            'msg' : '소환사가 없거나 언랭입니다.'
        }
    else:
    
        tier_rank = html.select_one('div.TierRankInfo .TierRank')
        league_points = html.select_one(' div.TierRankInfo > div.TierInfo > span.LeaguePoints')
        win = html.select_one('span.WinLose .wins')
        lose = html.select_one('span.WinLose .losses')
        winratio = html.select_one('span.WinLose .winratio')

        results ={
            'user' : user,
            'tier_rank' : tier_rank.text,
            'league_points' :league_points.text,
            'win' : win.text,
            'lose' : lose.text,
            'winratio' : winratio.text
        }

    return render(request,'ratio.html', results)