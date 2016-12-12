import requests
from bs4 import BeautifulSoup

url="https://www.yelp.com/san-jose"
r=requests.get(url)

soup=BeautifulSoup(r.content,'html.parser')
soup.prettify()

links = soup.find_all("a")
#for link in links:

#    print("<a href = '%s'>%s</a>" %(link.get("href"),link.text))

g_data = soup.find_all("div", {"class":"content"})
#print(g_data)
for item in g_data:
    print(item.text)
