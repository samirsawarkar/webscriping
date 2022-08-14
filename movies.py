import requests
from bs4 import BeautifulSoup
  
URL = "https://9xmovies.yoga/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
table = soup.find('div', attrs = {'class':'thumb col-md-2 col-sm-4 col-xs-6'}) 

print(table.find('img')['src'])
print(table.find('img')['alt'])
print(table.find('a')['href'])
