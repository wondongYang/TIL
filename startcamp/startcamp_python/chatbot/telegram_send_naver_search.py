import requests

# 기본 설정
TOKEN = '1768686612:AAHScZTLICbTj7Hw5KCeZw_o3a1smL51D0Y'
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

# chat_id 가져오기
# https://api.telegram.org/bot1768686612:AAHScZTLICbTj7Hw5KCeZw_o3a1smL51D0Y/getupdates

UPDATES_URL = f'{APP_URL}/getUpdates'
response = requests.get(UPDATES_URL).json()

chat_id = response.get('result')[0].get('message').get('chat').get('id')
print(chat_id)

# naver 요청 보낼 때 필요한 것들
naver_client_id = '0eUCMN4kPGsa_vUriLSA'
naver_client_secret = 'HWBsqipn7q'
URL = 'https://openapi.naver.com/v1/search/shop.json?query='

headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}

query = 'ps5'

product = requests.get(URL+query, headers=headers).json()['items'][0]
# print(product)

product_name = product['title']
# print(product_name)
product_price = product['lprice']
# print(product_price)
product_link = product['link']
# print(product_link)

message = f'{product_name}\n{product_price}\n{product_link}'
# print(message)

text = f'{message}.'

# https://api.telegram.org/bot1768686612:AAHScZTLICbTj7Hw5KCeZw_o3a1smL51D0Y/sendmessage?chat_id=1893246898&text=%EB%B0%B0%EA%B3%A0%ED%94%84%EB%84%A4%EC%9A%94
message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)