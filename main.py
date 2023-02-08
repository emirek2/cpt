import random
player_play=True
dealer_play=True


deck =[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
      "J","Q","K","A"]
dealer=[]
player=[]


#Assign the cards 
def assign(turn):
  card=random.choice(deck)
  turn.append(card)
  deck.remove(card)

#calculate the total
def total(turn):
  the_total=0
  face=['J','Q','K']
  for card in turn:
    if card in range (1,11):
      the_total+=card
    elif card in face:
      the_total+=1
    else:
      if the_total>11:
        the_total+=1
      else:
        the_total+=11
  return the_total


def dealer_hand():
  if len(dealer)==2:
    return dealer[0]
  elif len(dealer)>2:
    return dealer[0], dealer[1] 


#game start
for i in range(2):
  assign(dealer)
  assign(player)

while player_play or dealer_play:
  print(f'The dealer had {dealer_hand()} and X')
  print(f'You have {player} for a total of {total(player)}')
  if player_play:
    stay_hit=input("S:stay or H:hit ----")
    stay_hit.lower()
  if total(dealer)>17:
    dealer_play=False
  else:
    assign(dealer)
  if stay_hit=='s':
    player_play=False
  else:
    assign(player)
  if total(player)>=21:
    break
  elif total(dealer)>=21:
    break




# Now we are going to make conditions for winning
if total(player)==21:
  print(f"\nYou have a total of {total(player)} and the dealer has {total(dealer)}.")
  print('You win!!!! Blackjack.')
elif total(dealer)==21:
  print(f"\nYou have a total of {total(player)} and the dealer has {total(dealer)}.")
  print('You Lose:( Blackjack.')
elif total(player)>21:
  print(f"\nYou have a total of {total(player)} and the dealer has {total(dealer)}.")
  print('You lose:( Bust.')
elif total(dealer)>21:
  print(f"\nYou have a total of {total(player)} and the dealer has {total(dealer)}.")
  print('You Win!!!! Dealer Bust.')
elif total(player)>total(dealer):
  print(f"\nYou have a total of {total(player)} and the dealer has {total(dealer)}.")
  print('You Win!!!!')
elif total(player)<total(dealer):
  print(f"\nYou have a total of {total(player)} and the dealer has {total(dealer)}.")
  print('You Lose:(')