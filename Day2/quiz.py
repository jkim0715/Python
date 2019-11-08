import json
import requests
import time
#Quiz

# 1. 평균을 구하세요
scores ={
    "수학" : 90,
    "영어" : 87,
    "한국지리 " : 92
}

sum=0
for key, value in scores.items():
    sum=sum+value
avg1=sum/len(scores.keys())
print(avg1)


# 2. 각 학생의 평균 점수와 반 평균을 구하세요 
scores = {
    "a학생" : {
        "수학" : 80,
        "국어" : 90,
        "음악" : 100
    },
     "b학생" : {
        "수학" : 100,
        "국어" : 100,
        "음악" : 100
    }
}
# Key : {a학생 , b학생}
    #수,국,음 80 90 100
for value in scores.values():
    for val in value.values():
        sum = sum + val
    avg = sum/len(value.values())
    sum = 0    
    print(avg)



url ="http://webtoon.daum.net/data/pc/webtoon/list_serialized/thu?timeStamp=1573024597086"
response = requests.get(url)
#응답으로 온 내용을 바로json으로 바꿔줌
data = response.json()
print(type(data))

# 3. 다음 웹툰의 금요일 웹툰 전체의 리스트 중에서 각 웹툰의 제목, 설명, 작가이름, 장르, 썸네일 이미지(주소)만 골라새로운 dictionary를 만들고 이 dictionary를 담고 있는 list를 만드시오
# for d in data.keys():
print(type(data["data"]))    
webtoon_data = data["data"]

toons = []
for toon in  webtoon_data:
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

print(toons) 
 # 3-1. 금요일 뿐만 아니라 일요일부터 토요일까지의 웹툰 데이터를 파싱해서 각각 dictionary로 만드세요


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




#format string
days = ['mon',
    'tue',
    'wed',
    'thu',
    'fri',
    'sat',
    'sun']

daily_toon_data = {}
for day in days:
    url = f"http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}?timeStamp=1573024597086"
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    print(daily_toon_data[day])
    time.sleep(3)

