import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのliタグを検索して、その文字列を表示する
for element in soup.find_all("li"):    # すべてのliタグを検索して表示
    print(element.text)


# IDで検索して、そのタグの中身を表示する
chap2 = soup.find(id="chap2")    # idが「chap2」の範囲の要素を表示
print(chap2)
#
# 要素 = soup.find(class_="class名")
# ※「class」はPythonの予約語でそのままでは使えないので「class_」と書きます。
