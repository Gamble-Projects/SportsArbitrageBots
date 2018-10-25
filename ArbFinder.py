from data import data

# Variables
totalRisk = 1000
books = [
  # 'open',
  'VIConcensus',
  'Westgate',
  'MGM',
  'WilliamHill',
  'WynnLV',
  'CGTech',
  'Stations',
  'BetOnline',
  'GoldenNugget',
  'TreasureIsland',
  'SouthPoint',
  'Peppermill',
  'AtlantisReno',
  'Stratosphere',
  'Caesars',
  'JerrysNugget',
  'CoastsCasino'
]

# Calculate if Arbitrage Exists
def arbitrageCalculator(game, book1, book2):

  away = (game['away_team'], game[book1]['away'], game[book2]['away'])
  home = (game['home_team'], game[book1]['home'], game[book2]['home'])

  # Calculate Inversions
  L1 = (1 / home[1]) + (1 / away[2])
  L2 = (1 / home[2]) + (1 / away[1])

  # Checking both Inversions
  if L1 < 1:

    # Calculating Risk Amount for each Book
    BET1 = (totalRisk / (L1 * away[2]), away[0], away[2], book2)
    BET2 = (totalRisk / (L1 * home[1]), home[0], home[1], book1)

    # Calculating profit
    P = (BET1[0] * away[2]) - (BET1[0] + BET2[0])

    printStatements(L1, BET1, BET2, P)

  elif L2 < 1:

    # Calculating Risk Amount for each Book
    BET1 = (totalRisk / (L2 * away[1]), away[0], away[1], book1)
    BET2 = (totalRisk / (L2 * home[2]), home[0], home[2], book2)

    # Calculating profit
    P = (BET1[0] * away[1]) - (BET1[0] + BET2[0])

    printStatements(L2, BET1, BET2, P)

  else:
    print('No Arbitrage Detected :(')
    # pass


def printStatements(L, BET1, BET2, P):
  # print('\n')
  print('--------------------------------')
  print('🚨 🚨 ARBITRAGE ALERT !!! 🚨 🚨 ')
  print("Inversion: " + str(L)[:4])
  print('Bet $' + str(round(BET1[0], 2)) + ' on ' + BET1[1] + ' (' + str(BET1[2]) + ') with ' + BET1[3])
  print('Bet $' + str(round(BET2[0], 2)) + ' on ' + BET2[1] + ' (' + str(BET2[2]) + ') with ' + BET2[3])
  print('You will win $' + str(round(P, 2)))
  # print('--------------------------------')
  # print('\n')


# Main function to detect arbitrage and decide wager amounts
def Main():

  for key, value in data.items():

    print(key)

    for i in range(0, len(books)):
      for j in range(i+1, len(books)):
        book1 = books[i]
        book2 = books[j]
        arbitrageCalculator(value, book1, book2)


Main()