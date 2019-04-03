import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://www.espncricinfo.com/series/19059/game/1168247/india-vs-australia-1st-t20i-aus-in-ind-2018-19')
html = response.read()
# print(html)
soup = BeautifulSoup(html,'html.parser')
print(soup)
price_box = soup.find('div', attrs={'class':'cscore'})
price = price_box.text
print(price)
# save the data in tuple
# meta_content = soup.find('meta content')
# meta_data = meta_content # strip() is used to remove starting and trailing
# print(meta_data)



