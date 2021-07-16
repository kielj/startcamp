import requests
import json

serviceKey = 'P8f%2BfF55z%2BXc91%2B566%2FT9Sw5%2FhJ7W7xQDu%2BGUo196e03LkZ4vKzizKOOQHDe78SENB%2FEjkhK%2Fdb6JctcHSnBxg%3D%3D'
sidoName = '대구'
returnType = 'json'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={serviceKey}&sidoName={sidoName}&returnType={returnType}'

response = requests.get(url).text
data = json.loads(response)

san = data['response']['body']['items'][8]
result = san['pm10Value']
print(f'현재 대구 산격동 미세먼지 농도는 {result} 입니다.')
