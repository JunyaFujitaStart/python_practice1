import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://dq10ragu.com/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
print(soup)
# すべてのliタグを検索して、その文字列を表示する
# for element in soup.find_all("li"):    # すべてのliタグを検索して表示
#     print(element.text)

# print('ここで区切り')
# IDで検索して、そのタグの中身を表示する
chap2 = soup.find(class_="clearfix")    # idが「chap2」の範囲の要素を表示
# for chap3 in chap2.find_all("h3"): # すべてのliタグを検索して表示
#     chap4=chap3.get('href')
print(chap2)
#
# 要素 = soup.find(class_="class名")
# ※「class」はPythonの予約語でそのままでは使えないので「class_」と書きます。
