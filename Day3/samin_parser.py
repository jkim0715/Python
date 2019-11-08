from bs4 import BeautifulSoup
import requests

url = 'http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&tab_type=all&panel_type=&search_optional_item=n&search_done=y&panel_count=y&smart_tag='
response = requests.get(url)

# BeautifulSoup이 먼저 html 을 한번 읽는 과정
html = BeautifulSoup(response.text ,'html.parser')
# copy selector 
# banner_list > div:nth-child(2) > ul:nth-child(3) > li:nth-child(4) > div.part_top > h3

#company_name이라고 하는 class를 가진 모든 친구들 select.
company_names = html.select('.company_name')
recruit_names = html.select('.recruit_name')
recruit_conditions = html.select('.list_recruit_condition')

'''
for company_name in company_names:
    print(company_name.text)

for recruit_name in recruit _ names:
    print(recruit_name.text)


for company_name, recruit_name, condition in zip(company_names, recruit_names, recruit_conditions):
    print(f'{company_name.text}-{recruit_name.text}')
    print(condition.text)


company = html.select('.part_top')
for com in company:
    print(f'{com.select_one(".company_name").text} - {com.select_one(".recruit_name").text}')
    #print(com.select_one('.list_recruit_condition').text)

    break
'''


company_list = html.select('ul.product_list li' )
for com in company_list:
    #하나만 뽑아봅시다.
    idx = com.select_one('a')['href'].split('=')[-1]
    company_info_url ='http://www.saramin.co.kr/zf_user/jobs/relay/view-ajax'
    company_info_params = { 'rec_idx': idx }
    
    #post 방식으로 request 보내야 할 때(requests.post). parameter도 따로 보내줘야 됨.
    company_response = requests.post(company_info_url, params=company_info_params)
    # Tag로 찾을 수 있게끔 Bs4로 파싱
    company_html = BeautifulSoup(company_response.text, 'html.parser')
    company_title = company_html.select_one('a.company').text
    print(company_title.strip())
    break

