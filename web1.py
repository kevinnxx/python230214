#web1.py
from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html", "rt", encoding="utf-8")
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
# print(soup.find_all("p"))
#print(soup.find_all("a"))
#print(soup.find_all("p", class_ = "outer-text"))

#태그 내부의 문자열: .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)