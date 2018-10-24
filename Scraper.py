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

gameData = []

for game in games:
  links = game.find_all('a')
  gameDataObj = {
      'away_team': links[0].get_text().strip(),
      'home_team': links[1].get_text().strip(),
      'open_odds': links[2].get_text().strip(),
      'VIConcensus_odds': links[3].get_text().strip(),
      'Westgate_odds': links[4].get_text().strip(),
      # 'MGM_odds': links[5].get_text().strip(),
      'WilliamHill_odds': links[5].get_text().strip(),
      'WynnLV_odds': links[6].get_text().strip(),
      'CDTech_odds': links[7].get_text().strip(),
      'Stations_odds': links[8].get_text().strip(),
      'BetOnline_odds': links[9].get_text().strip()
    }
  gameData.append(gameDataObj)
  # print(gameDataObj)
  # print('--------------------------------------------------')

# print(gameData)