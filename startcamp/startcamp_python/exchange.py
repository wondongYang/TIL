# 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange_A = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result_A = exchange_A.text
exchange_J = data.select_one('#worldExchangeList > li.on > a.head.jpy_usd > div > span.value')
result_J = exchange_J.text


print(f'현재 원/달러 환율은 {result_A}입니다.')
print(f'현재 원/엔 환율은 {result_J}입니다.')