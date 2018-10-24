MLhome1 = +282
MLaway1 = -357
MLhome2 = +150
MLaway2 = -170

# Convert American Odds to Decimal Odds
def convert(moneyline):
  if moneyline > 0:
    return ((moneyline/100) + 1)
  elif moneyline < 0:
    return (-1 * ((100/moneyline) - 1))
  else:
    print('Problem')

home1 = convert(MLhome1)
away1 = convert(MLaway1)
home2 = convert(MLhome2)
away2 = convert(MLaway2)

print( (home1, away1), (home2, away2))

totalRisk = 1000

def ArbDetector(home1, away1, home2, away2):

  L1 = (1/home1) + (1/away2)
  L2 = (1/home2) + (1/away1)

  # Inversion 1
  if L1 < 1:
    print('🚨 🚨 ARBITRAGE ALERT @ ' + str(L1) + ' !!!🚨 🚨 ')

    BET1 = totalRisk / (L1 * home1)
    BET2 = totalRisk / (L1 * away2)
    print('Bet $' + str(round(BET1, 2)) + ' on the HOME team on BOOK 1')
    print('Bet $' + str(round(BET2, 2)) + ' on the AWAY team on BOOK 2')

    P1 = (BET1 * home1) - (BET1 + BET2)
    P2 = (BET2 * away2) - (BET1 + BET2)
    print('If HOME wins, you will win ' + str(P1))
    print('If AWAY wins, you will win ' + str(P2))

  # Inversion 2
  elif L2 < 1:
    print('🚨 🚨 ARBITRAGE ALERT @ ' + str(L2) + ' !!!🚨 🚨 ')

    BET1 = totalRisk / (L2 * home2)
    BET2 = totalRisk / (L2 * away1)
    print('Bet $' + str(round(BET1, 2)) + ' on the HOME team on BOOK 2')
    print('Bet $' + str(round(BET2, 2)) + ' on the AWAY team on BOOK 1')

    P1 = (BET1 * home2) - (BET1 + BET2)
    P2 = (BET2 * away1) - (BET1 + BET2)
    print('If HOME wins, you will win $' + str(round(P1, 2)))
    print('If AWAY wins, you will win $' + str(round(P2, 2)))

  # No Arbitrage
  else:
    print('No Arbitrage Detected :(')
  

ArbDetector(home1, away1, home2, away2)

# def Bets(totalRisk, Arb, Odds1, Odds2):
#   print(totalRisk, Arb, Odds1, Odds2)

# def Main():
#   Inversion(home1, away1, home2, away2)
#   Bets(totalRisk, Arb, Odds1, Odds2)
# Main()