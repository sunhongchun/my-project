import requests

url = "http://www.cntour.cn/"
response = requests.get(url)
response = response.text
print(response)

