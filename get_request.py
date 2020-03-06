import requests

url = "https://www.baidu.com"
response = requests.get(url)
response = response.text
print(response)

