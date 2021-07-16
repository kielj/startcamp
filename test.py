import requests
import json

serviceKey = 'P8f%2BfF55z%2BXc91%2B566%2FT9Sw5%2FhJ7W7xQDu%2BGUo196e03LkZ4vKzizKOOQHDe78SENB%2FEjkhK%2Fdb6JctcHSnBxg%3D%3D'
sidoName = '대구'
sidoName2 = '서울'
returnType = 'json'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={serviceKey}&sidoName={sidoName}&returnType={returnType}'
url2 = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={serviceKey}&sidoName={sidoName2}&returnType={returnType}'

response = requests.get(url).text
response2 = requests.get(url2).text
data = json.loads(response)
data2 = json.loads(response2)

san = data['response']['body']['items'][8]
seoul = data2['response']['body']['items'][1]
result = san['pm10Value']
result2 = seoul['pm10Value']
test = input()
if test == '미세먼지대구':
    print(f'현재 대구 산격동 미세먼지 농도는 {result} 입니다.')
elif test == '미세먼지서울':
    print(f'현재 서울 미세먼지 농도는 {result2} 입니다.')
