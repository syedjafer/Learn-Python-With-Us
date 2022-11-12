from bs4 import BeautifulSoup as bs
import requests
word=input("enter the word to search: ")
url = "https://www.google.com/search?q="+word+"&tbm=nws"
content=requests.get(url).text
soup = bs(content, 'lxml')

for item in soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd"):
    print(item.text)
    print()


