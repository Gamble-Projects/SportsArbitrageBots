from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/money/?s=75'

# Opening connection and grabbing page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# HTML Parser
soup = BeautifulSoup(page_html, "html.parser")

data = soup.find("table", {"class": "frodds-data-tbl"})

rows = data.find_all("tr")

# for game in rows:
#   print(game)
#   print('\n--------------------------------------------------\n')

count = 0
games = []
for row in rows:
  if count % 2 == 0:
    games.append(row)
  count += 1

for game in games:
  away = game.find('a').get_text()
  home = game.find('a').get_text()
  print(away, home)    
  print('--------------------------------------------------')
