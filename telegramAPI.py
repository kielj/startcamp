import requests
token = '1851167299:AAFO4yxT9Egg_3sy4JY7FSFQL37yrv2ukDQ'
url = f'https://api.telegram.org/bot{token}'
update_url = f'{url}/getUpdates'

# print(update_url)
# print(message_url)

response = requests.get(update_url).json()

result = response['result']

chat_id = result[-1]['message']['chat']['id']

# print(chat_id)

text = '이거는 파이썬에서 보내는 메세지입니다.'
message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)
