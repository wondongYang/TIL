import requests
from bs4 import BeautifulSoup

# 요청을 보낼 url
url = 'https://finance.naver.com/marketindex/'

# 실제 요청을 보내고, 응답 객체를 response 변수에 저장
response = requests.get(url)

# 응답 객체의 본문(text)을 해석하여 data 변수에 저장
data = BeautifulSoup(response.text, 'html.parser')

# 해석한 data에서 원하는 정보를 선택하고, 내용만 exchange에 저장
exchange_us = data.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value').text

print(exchange_us)