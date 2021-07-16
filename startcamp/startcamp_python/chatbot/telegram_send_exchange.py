import requests
from bs4 import BeautifulSoup

# 기본 설정
TOKEN = '1768686612:AAHScZTLICbTj7Hw5KCeZw_o3a1smL51D0Y'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

# chat_id 가져오기
# https://api.telegram.org/bot1768686612:AAHScZTLICbTj7Hw5KCeZw_o3a1smL51D0Y/getupdates

UPDATES_URL = f'{APP_URL}/getUpdates'
response = requests.get(UPDATES_URL).json()

chat_id = response.get('result')[0].get('message').get('chat').get('id')
print(chat_id)

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange_A = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result_A = exchange_A.text
exchange_J = data.select_one('#worldExchangeList > li.on > a.head.jpy_usd > div > span.value')
result_J = exchange_J.text

print(f'현재 원/달러 환율은 {result_A}입니다.')
print(f'현재 원/엔 환율은 {result_J}입니다.')

message = f'현재 원/달러 환율은 {result_A}입니다.\n현재 원/엔 환율은 {result_J}입니다.'

text = f'{message}'

# https://api.telegram.org/bot1768686612:AAHScZTLICbTj7Hw5KCeZw_o3a1smL51D0Y/sendmessage?chat_id=1893246898&text=%EB%B0%B0%EA%B3%A0%ED%94%84%EB%84%A4%EC%9A%94
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)