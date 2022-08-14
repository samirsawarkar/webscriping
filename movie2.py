import requests
from bs4 import BeautifulSoup
  
URL = "https://9xmovies.yoga/goto/goyKY4EDcoXYcy3F7nv1gjlwAMftJ8zNR4tqahSB7Sd3uuR2bWot+CwfkwqYTbKf:Q8tu86JPiH+JNJdYXnd4cQ=="
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
table = soup.find('div', attrs = {'align':'center'}) 
print(table.find('a')['href'])