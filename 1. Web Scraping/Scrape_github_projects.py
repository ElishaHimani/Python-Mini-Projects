import requests
from bs4 import BeautifulSoup as bs

i = 1
github_username = input('Input Github Username: ')
url = 'https://github.com/'+github_username+'?tab=repositories'
requested_url = requests.get(url)
soup = bs(requested_url.content, 'html.parser')
project_name = soup.find_all('a', {'itemprop':'name codeRepository'})

for urls in project_name:
    url = urls['href']
    print(i, urls.string,'-', 'https://github.com'+url)
    i += 1

  

