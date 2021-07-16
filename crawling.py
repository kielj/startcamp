import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/').text
# print(response)

data = BeautifulSoup(response, 'html.parser')

k_value = data.select_one('#KOSPI_now').text
# result = k_value.text
print(f'코스피 지수 : {k_value}')
