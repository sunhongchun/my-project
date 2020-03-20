from typing import Dict, Any

import requests
from bs4 import BeautifulSoup

url = "http://www.cntour.cn/"
response = requests.get(url)

# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select("#main > div > div.newListBox.clearfix > div.leftBox"
                   "div.newsList > ul > li:nth-child(9) > a")
print(data)

# for item in data:
#     result = {
#         'title': item.get_text(),
#         'link': item.get('href')
#     }
# print(result)
