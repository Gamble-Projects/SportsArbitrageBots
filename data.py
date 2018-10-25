from ScrapeVi1 import gameData as gameData1
from ScrapeVi2 import gameData as gameData2
import pprint

data = {}

for game in gameData1:
  matchup = game['away_team'] + ' @ ' + game['home_team']
  data[matchup] = game

for game in gameData2:
  matchup = game['away_team'] + ' @ ' + game['home_team']
  for key, value in game.items():
    data[matchup][key] = value

# pprint.pprint(data)