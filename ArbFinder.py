from Scraper import gameData

# print(gameData)

# Convert American Odds to Decimal Odds
def convert(moneyline):
  if moneyline > 0:
    return ((moneyline / 100) + 1)
  elif moneyline < 0:
    return ((100 / (-1 * moneyline)) + 1)
  else:
    print('Problem')

# Main function to detect arbitrage and decide wager amounts
def ArbDetector():

  totalRisk = 100

  for game in gameData:

    print('\n')
    print(game['away_team'] + ' vs. ' + game['home_team'])
    
    books = [
      'open_odds',
      'VIConcensus_odds',
      'Westgate_odds',
      'WilliamHill_odds',
      'WynnLV_odds',
      'CDTech_odds',
      'Stations_odds',
      'BetOnline_odds'
      ]

    for i in range(0, len(books)):
      for j in range(i+1, len(books)):

        book1_name = books[i]
        book2_name = books[j]

        book1 = game[books[i]]
        book2 = game[books[j]]

        try:
          MLhome1 = int(game[books[i]][:4])
          MLaway1 = int(game[books[i]][4:])
          MLhome2 = int(game[books[j]][:4])
          MLaway2 = int(game[books[j]][4:])
        except:
          continue

        home1 = convert(MLhome1)
        away1 = convert(MLaway1)
        home2 = convert(MLhome2)
        away2 = convert(MLaway2)

        L1 = (1/home1) + (1/away2)
        L2 = (1/home2) + (1/away1)

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
          print('Bet $' + str(round(BET1, 2)) + ' on ' + game['home_team'] + ' on ' + book1_name)
          print('Bet $' + str(round(BET2, 2)) + ' on ' + game['away_team'] + ' on ' + book2_name)

          P1 = (BET1 * home1) - (BET1 + BET2)
          P2 = (BET2 * away2) - (BET1 + BET2)
          print('If HOME wins, you will win $' + str(round(P1, 2)))
          print('If AWAY wins, you will win $' + str(round(P2, 2)))

        # Inversion 2
        elif L2 < 1:
          print('🚨 🚨 ARBITRAGE ALERT @ ' + str(L2) + ' !!!🚨 🚨 ')

          BET1 = totalRisk / (L2 * home2)
          BET2 = totalRisk / (L2 * away1)
          print('Bet $' + str(round(BET1, 2)) + ' on ' + game['home_team'] + ' on ' + book2_name)
          print('Bet $' + str(round(BET2, 2)) + ' on ' + game['away_team'] + ' on ' + book1_name)

          P1 = (BET1 * home2) - (BET1 + BET2)
          P2 = (BET2 * away1) - (BET1 + BET2)
          print('If HOME wins, you will win $' + str(round(P1, 2)))
          print('If AWAY wins, you will win $' + str(round(P2, 2)))

        # No Arbitrage
        else:
          print('No Arbitrage Detected :(')
    
ArbDetector()