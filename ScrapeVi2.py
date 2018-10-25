from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

my_url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/money/2/'

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
    GoldenNugget_away = re.findall(regExOdds, cells[1].get_text().strip())[0]
    GoldenNugget_home = re.findall(regExOdds, cells[1].get_text().strip())[1]
  except:
    GoldenNugget_away = 0
    GoldenNugget_home = 0

  try:
    TreasureIsland_away = re.findall(regExOdds, cells[2].get_text().strip())[0]
    TreasureIsland_home = re.findall(regExOdds, cells[2].get_text().strip())[1]    
  except:
    TreasureIsland_away = 0
    TreasureIsland_home = 0

  try:
    SouthPoint_away = re.findall(regExOdds, cells[3].get_text().strip())[0]
    SouthPoint_home = re.findall(regExOdds, cells[3].get_text().strip())[1]
  except:
    SouthPoint_away = 0
    SouthPoint_home = 0

  try:
    Peppermill_away = re.findall(regExOdds, cells[4].get_text().strip())[0]
    Peppermill_home = re.findall(regExOdds, cells[4].get_text().strip())[1]
  except:
    Peppermill_away = 0
    Peppermill_home = 0

  try:
    AtlantisReno_away = re.findall(regExOdds, cells[5].get_text().strip())[0]
    AtlantisReno_home = re.findall(regExOdds, cells[5].get_text().strip())[1]
  except:
    AtlantisReno_away = 0
    AtlantisReno_home = 0

  try:
    Stratosphere_away = re.findall(regExOdds, cells[6].get_text().strip())[0]
    Stratosphere_home = re.findall(regExOdds, cells[6].get_text().strip())[1]
  except:
    Stratosphere_away = 0
    Stratosphere_home = 0

  try:
    Caesars_away = re.findall(regExOdds, cells[7].get_text().strip())[0]
    Caesars_home = re.findall(regExOdds, cells[7].get_text().strip())[1]
  except:
    Caesars_away = 0
    Caesars_home = 0

  try:
    JerrysNugget_away = re.findall(regExOdds, cells[8].get_text().strip())[0]
    JerrysNugget_home = re.findall(regExOdds, cells[8].get_text().strip())[1]
  except:
    JerrysNugget_away = 0
    JerrysNugget_home = 0

  try:
    CoastsCasino_away = re.findall(regExOdds, cells[9].get_text().strip())[0]
    CoastsCasino_home = re.findall(regExOdds, cells[9].get_text().strip())[1]
  except:
    CoastsCasino_away = 0
    CoastsCasino_home = 0

  gameDataObj = {
      'away_team': away_team,
      'home_team': home_team,
      'GoldenNugget': {
        'away': convertAmericanToDecimal(GoldenNugget_away),
        'home': convertAmericanToDecimal(GoldenNugget_home)
      },
      'TreasureIsland': {
        'away': convertAmericanToDecimal(TreasureIsland_away),
        'home': convertAmericanToDecimal(TreasureIsland_home)
      },
      'SouthPoint': {
        'away': convertAmericanToDecimal(SouthPoint_away),
        'home': convertAmericanToDecimal(SouthPoint_home)
      },
      'Peppermill': {
        'away': convertAmericanToDecimal(Peppermill_away),
        'home': convertAmericanToDecimal(Peppermill_home)
      },
      'AtlantisReno': {
        'away': convertAmericanToDecimal(AtlantisReno_away),
        'home': convertAmericanToDecimal(AtlantisReno_home)
      },
      'Stratosphere': {
        'away': convertAmericanToDecimal(Stratosphere_away),
        'home': convertAmericanToDecimal(Stratosphere_home)
      },
      'Caesars': {
        'away': convertAmericanToDecimal(Caesars_away),
        'home': convertAmericanToDecimal(Caesars_home)
      },
      'JerrysNugget': {
        'away': convertAmericanToDecimal(JerrysNugget_away),
        'home': convertAmericanToDecimal(JerrysNugget_home)
      },
      'CoastsCasino': {
        'away': convertAmericanToDecimal(CoastsCasino_away),
        'home': convertAmericanToDecimal(CoastsCasino_home)
      }
    }
  gameData.append(gameDataObj)

# for game in gameData:
#   print(game)
#   print('\n')