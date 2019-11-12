from flask import Flask, request, render_template, redirect, url_for
import requests
import json

app = Flask(__name__)


#1. 전체 요일 적혀있는 페이지
@app.route('/')
def index():
    days ={
        '월요일': 'mon',
        '화요일': 'tue',
        '수요일': 'wed',
        '목요일': 'thu',
        '금요일': 'fri',
        '토요일': 'sat',
        '일요일': 'sun',
    }
    return render_template('index.html' , **locals())

#2. 각 요일에 대한 데이터 요청하는 곳
#2-1. path param으로 되어있는 Daum을 쓰고있기 때문에 우리도 path param을 사용.
# @app.route('/<day>')
# def day_webtoon_list(day):
#     url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
#     response = requests.get(url)
#     data = response.json()
#     webtoons={}
#     for toon in data["data"]:
#         webtoon_title = toon['title']
#         webtoon_nickname = toon['nickname']
#         webtoon_introduction = toon['introduction']
#         webtoon_artists = []
#         for artist in toon['cartoon']['artists']:
#             webtoon_artists.append(artist['name'])
        
#         webtoons[webtoon_title] =[webtoon_nickname,webtoon_introduction, ",".join(webtoon_artists)]

#     return render_template('day_webtoon_list.html', webtoon_dict = webtoons)

#3. 각 웹툰에 대한 세부 데이터 요청하는 곳.
@app.route('/webtoon/<nickname>')
def webtoon_info(nickname):
    url =f'http://webtoon.daum.net/data/pc/webtoon/view/{nickname}'
    return requests.get(url).json()


#4. form Data fake search
@app.route('/naver')
def fake_naver():
    return render_template('naver.html')

@app.route('/naver/search')
def fake_naver_search():
    #검색 로직
    #querystring의 값을 받아온 후 다시 뿌려주면 됨
    query = request.args.get('query')
    return render_template('search.html', q= query)


#5. fake login
@app.route('/login')
def fake_login_form():
    return render_template('login.html')
    #아이디 입력창, 패스워드 입력창, 로그인 버튼

@app.route('/login/submit' , methods=['POST'])
def fake_login_submit():
    #아이디를 조회하고 해당 row의 비밀번호가 일치하는지 
    #로그인 로직
    
    return redirect(url_for('main'))

    # return render_template('success.html') 만약에 랜더링을 시키면 POST방식이기 때문에 새로고침 했을때 문제가 생길 수있으므로 redirect추천. 

@app.route('/main')
def main():
    return '로그인 성공'