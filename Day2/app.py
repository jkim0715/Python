#실행준비
from flask import Flask, escape, request
import json
import requests

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)
# 요청받는 경로 및 리턴경로 설정


def request_json_data_from_url(url):
    response= requests.get(url)
    data = response.json()
    return data

def parse_daum_webtoon_data(data):
    toons = []
    for toon in data["data"]:
        #제목의 key 는 title
        title = toon["title"]
        #설명의 key는 introduction
        desc = toon["introduction"]


        #장르의 위치는 'cartoon'안에 'genre'라는 리스트 안에 'name'이라는 key
        genres = []
        for genre in toon["cartoon"]["genres"]:
            genres.append(genre["name"])

        artist = []
        for author in toon["cartoon"]["artists"]:
            artist.append(author["name"])

        img_url = toon["pcThumbnailImage"]["url"]
    
        tmp = {
            title : {
                "desc" : desc,
                "author" : artist,
                "img_url" : img_url
            }
        }
        toons.append(tmp)
    return toons

@app.route('/')
def index():
    daily_toon_data = {}
    day = 'mon'
    url = f"http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}"
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    return daily_toon_data


