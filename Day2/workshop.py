import time
import json
import requests

def request_data_from_url(url)
    response = requests.get(url)
    data = response.json
    return data
def parse_naver_map_route(data)
    gil = [] 
    

