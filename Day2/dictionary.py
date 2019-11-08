import random

#dictionary 
#key:value
student_phone_number = {
    "김민지":"010-1234-1234"
}
print(student_phone_number["김민지"])
print(student_phone_number.get("김민지"))

#2중 dictionary
lunch_menu = {
    "20층 식당" : {
        "A코스" : "순대국",
        "B코스" : "돈까스"
    },
    "양자강" : {
        "점심메뉴" : "탕짬면",
        "특선메뉴" : "군만두"
    },
    "대동집" : {
        "밥안주" : "비빔면",
        "술안주" : "오돌뼈"
    }
}

print(lunch_menu["20층 식당"]["B코스"])
print(lunch_menu.get("20층 식당").get("B코스"))
# Dictionary에 Data 추가하기 
lunch_menu["경성불백"] = {
    "한식메뉴" : "석쇠불고기",
    "특식메뉴" : "돈까스" 
}

'''
print(lunch_menu)
## 주의!
lunch_menu["양자강"] = "짜장면"
## 이렇게 Key 값이 같은걸 추가하면 마지막으로 추가된 value로 Replace됨
print("-------------------------------------------------------")
print(lunch_menu)
'''

# 1. 모든 키값 뽑기 배열로 리턴됨.
lunch_menu.keys()
# 2. 모든 value 값 뽑기
lunch_menu.values()
# 3. 모든 Key : Value 뽑기
lunch_menu.items()

# 반복문 활용해서 값 뽑아오기
# Python for문 Scope은 :이랑 indent(tab) 로 구분
for key in lunch_menu.keys():
    print(key)
for key, value in lunch_menu.items():
    print(key, value)

#random활용
#choice 는 한개
#sample 은 여러개
#lunch_menu.keys() 이거 타입이 dics_keys로 되어있어서 바꿔줘야됨.
print(random.choice(list(lunch_menu.keys())))
print(random.sample( list(lunch_menu.keys()), 2))

##조건문
if 조건1:
    #조건1 실행문
elif 조건2:
    #조건2 실행문
else:
    #나머지 실행문

##함수 만드는 방법
def 함수명(파라미터):    