import requests
from bs4 import BeautifulSoup
  
URL = "https://9xmovies.yoga/minions-the-rise-of-gru-2022-dual-audio-hindi-720p-480p-web-dl-900mb-300mb/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
table = soup.find('section', attrs = {'class':'left-wrapper col-md-8'}) 
# print(table.findAll('img'))

# s = 0
# for i in table.findAll('img'):
#     s= s+1
#     gett = i.get('src')
#     if s == 2:
#         print(gett)
    
   
for i in table.findAll('a',attrs={ 'class':"maxbutton-24 maxbutton maxbutton-batch-zip"}):
    print(i.get('href'))
    