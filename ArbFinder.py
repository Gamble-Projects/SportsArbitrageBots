from Scraper import gameData

# print(gameData)

# Convert American Odds to Decimal Odds
def convert(str):
  moneyline = int(str)
  if moneyline > 0:
    return ((moneyline / 100) + 1)
  elif moneyline < 0:
    return ((100 / (-1 * moneyline)) + 1)
  else:
    print('Problem!')

# Main function to detect arbitrage and decide wager amounts
def ArbDetector():

  totalRisk = 100

  books = [
    'open',
    'VIConcensus',
    'Westgate',
    'MGM',
    'WilliamHill',
    'WynnLV',
    'CGTech',
    'Stations',
    'BetOnline'
  ]

  for game in gameData:

    # print(game)
    away_team = game['away_team']
    home_team = game['home_team']

    print('\n')
    print(away_team.upper() + ' vs. ' + home_team.upper())
  

    for i in range(0, len(books)):
      for j in range(i+1, len(books)):

        book1 = books[i]
        book2 = books[j]
        
        # print(book1 + book2)

        home1 = convert(game[book1]['home'])
        away1 = convert(game[book1]['away'])
        home2 = convert(game[book2]['home'])
        away2 = convert(game[book2]['away'])

        try:
          L1 = (1/home1) + (1/away2)
          L2 = (1/home2) + (1/away1)
        except:
          continue

        # print('\n')
        # print(books[i], book1)
        # print(books[j], book2)
        # print("Inversion 1: " + str(L1))
        # print("Inversion 2: " + str(L2))

        # Inversion 1
        if L1 < 1:
          print('🚨 🚨 ARBITRAGE ALERT @ ' + str(L1) + ' !!!🚨 🚨 ')

          BET1 = totalRisk / (L1 * home1)
          BET2 = totalRisk / (L1 * away2)
          print('Bet $' + str(round(BET1, 2)) + ' on ' + game['home_team'] + ' with ' + book1)
          print('Bet $' + str(round(BET2, 2)) + ' on ' + game['away_team'] + ' with ' + book2)

          P1 = (BET1 * home1) - (BET1 + BET2)
          P2 = (BET2 * away2) - (BET1 + BET2)
          print('If HOME wins, you will win $' + str(round(P1, 2)))
          print('If AWAY wins, you will win $' + str(round(P2, 2)))

        # Inversion 2
        elif L2 < 1:
          print('🚨 🚨 ARBITRAGE ALERT @ ' + str(L2) + ' !!!🚨 🚨 ')

          BET1 = totalRisk / (L2 * home2)
          BET2 = totalRisk / (L2 * away1)
          print('Bet $' + str(round(BET1, 2)) + ' on ' + game['home_team'] + ' with ' + book2)
          print('Bet $' + str(round(BET2, 2)) + ' on ' + game['away_team'] + ' with ' + book1)

          P1 = (BET1 * home2) - (BET1 + BET2)
          P2 = (BET2 * away1) - (BET1 + BET2)
          print('If HOME wins, you will win $' + str(round(P1, 2)))
          print('If AWAY wins, you will win $' + str(round(P2, 2)))

        # No Arbitrage
        else:
          print('No Arbitrage Detected :(')
    
ArbDetector()