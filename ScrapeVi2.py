from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

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

# Convert American Odds to Decimal Odds
def convertAmericanToDecimal(american):

  # print('American: ', american, type(american))

  americanOdds = int(american)
  
  if americanOdds > 0:
    decimalOdds = round(((americanOdds / 100) + 1), 3)
    
  elif americanOdds < 0:
    decimalOdds = round(((100 / (-1 * americanOdds)) + 1), 3)

  else:
    decimalOdds = round(1, 3)

  # print('Decimal: ', decimalOdds, type(decimalOdds))
  return decimalOdds



count = 0
games = []
for row in rows:
  if count % 2 == 0:
    games.append(row)
  count += 1

gameData = []
regExOdds = r"(.\d{3,5})"
regExTeam = r"[a-zA-Z]{1,15} ?[a-zA-Z]{3,15}"

for game in games:
  # print(game)
  # print('--------------------------')

  cells = game.find_all('td')

  away_team = re.findall(regExTeam, cells[0].get_text().strip())[0]
  home_team = re.findall(regExTeam, cells[0].get_text().strip())[1]

  try:
    open_away = re.findall(regExOdds, cells[1].get_text().strip())[0]
    open_home = re.findall(regExOdds, cells[1].get_text().strip())[1]
  except:
    open_away = 0
    open_home = 0

  try:
    VIConcensus_away = re.findall(regExOdds, cells[2].get_text().strip())[0]
    VIConcensus_home = re.findall(regExOdds, cells[2].get_text().strip())[1]    
  except:
    VIConcensus_away = 0
    VIConcensus_home = 0

  try:
    Westgate_away = re.findall(regExOdds, cells[3].get_text().strip())[0]
    Westgate_home = re.findall(regExOdds, cells[3].get_text().strip())[1]
  except:
    Westgate_away = 0
    Westgate_home = 0

  try:
    MGM_away = re.findall(regExOdds, cells[4].get_text().strip())[0]
    MGM_home = re.findall(regExOdds, cells[4].get_text().strip())[1]
  except:
    MGM_away = 0
    MGM_home = 0

  try:
    WilliamHill_away = re.findall(regExOdds, cells[5].get_text().strip())[0]
    WilliamHill_home = re.findall(regExOdds, cells[5].get_text().strip())[1]
  except:
    WilliamHill_away = 0
    WilliamHill_home = 0

  try:
    WynnLV_away = re.findall(regExOdds, cells[6].get_text().strip())[0]
    WynnLV_home = re.findall(regExOdds, cells[6].get_text().strip())[1]
  except:
    WynnLV_away = 0
    WynnLV_home = 0

  try:
    CGTech_away = re.findall(regExOdds, cells[7].get_text().strip())[0]
    CGTech_home = re.findall(regExOdds, cells[7].get_text().strip())[1]
  except:
    CGTech_away = 0
    CGTech_home = 0

  try:
    Stations_away = re.findall(regExOdds, cells[8].get_text().strip())[0]
    Stations_home = re.findall(regExOdds, cells[8].get_text().strip())[1]
  except:
    Stations_away = 0
    Stations_home = 0

  try:
    BetOnline_away = re.findall(regExOdds, cells[9].get_text().strip())[0]
    BetOnline_home = re.findall(regExOdds, cells[9].get_text().strip())[1]
  except:
    BetOnline_away = 0
    BetOnline_home = 0

  gameDataObj = {
      'away_team': away_team,
      'home_team': home_team,
      'open': {
        'away': convertAmericanToDecimal(open_away),
        'home': convertAmericanToDecimal(open_home)
      },
      'VIConcensus': {
        'away': convertAmericanToDecimal(VIConcensus_away),
        'home': convertAmericanToDecimal(VIConcensus_home)
      },
      'Westgate': {
        'away': convertAmericanToDecimal(Westgate_away),
        'home': convertAmericanToDecimal(Westgate_home)
      },
      'MGM': {
        'away': convertAmericanToDecimal(MGM_away),
        'home': convertAmericanToDecimal(MGM_home)
      },
      'WilliamHill': {
        'away': convertAmericanToDecimal(WilliamHill_away),
        'home': convertAmericanToDecimal(WilliamHill_home)
      },
      'WynnLV': {
        'away': convertAmericanToDecimal(WynnLV_away),
        'home': convertAmericanToDecimal(WynnLV_home)
      },
      'CGTech': {
        'away': convertAmericanToDecimal(CGTech_away),
        'home': convertAmericanToDecimal(CGTech_home)
      },
      'Stations': {
        'away': convertAmericanToDecimal(Stations_away),
        'home': convertAmericanToDecimal(Stations_home)
      },
      'BetOnline': {
        'away': convertAmericanToDecimal(BetOnline_away),
        'home': convertAmericanToDecimal(BetOnline_home)
      }
    }
  gameData.append(gameDataObj)

# for game in gameData:
#   print(game)
#   print('\n')