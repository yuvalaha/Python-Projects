############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
import art
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 



#printing function  
def printing(my_cards_score,computer_score):  
 if my_cards_score==21:
  if  computer_score==21:
    print("It's a draw")
  elif computer_score!=21:
     print("You Win 😃 ")
 elif my_cards_score>21:
   print("You went over. You lose 😭") 
 else:
  if my_cards_score>computer_score or computer_score>21:
    print("You Win 😃")
  elif my_cards_score==computer_score:   
    print("It's a draw")
  elif computer_score==21:
    print("Lose, opponent has Blackjack 😱")
  else:
    print("You lose 😭")
 ans=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
 if ans=='y':
   game()
   
#Compare score function
def check_score(my_cards,computer_score):
  computer_cards=[]
  computer_cards.append(computer_score)
  computer_score=sum(computer_cards)
  if computer_score==21:
    print("Lose, opponent has Blackjack 😱")
    return
  else:  
    while computer_score<=16:
      computer_cards.append(random.choice(cards))
      computer_score=sum(computer_cards)
    print(f"   Your final hand: {my_cards}, final score: {sum(my_cards)}")
    print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    my_score=sum(my_cards)
    printing(my_score,computer_score)

  #Drawing more cards function  
def draw_more_cards(my_cards,computer_score):
  my_cards.append(random.choice(cards))
  your_score=sum(my_cards)
  if your_score==21:
    check_score(my_cards,computer_score)
    return
  if your_score>=21 and 11 not in my_cards:
    check_score(my_cards,computer_score)
    return
  elif your_score>21 and 11 in my_cards:
      my_cards.remove(11)
      my_cards.append(1)
      your_score-=10
  print(f"   Your cards: {my_cards}, current score: {your_score}")
  print(f"   Computer's first card: {computer_score}")  
  another_card=input("Type 'y' to get another card, type 'n' to pass: ")
  if another_card =='y':
    draw_more_cards(my_cards,computer_score)
  else:
    check_score(my_cards,computer_score)

#A blackjack win  
def blackjack(my_cards,computer_score):
  print(f"   Your final hand: {my_cards}, final score: {sum(my_cards)}")
  computer_cards=[]
  computer_cards.append(computer_score)
  computer_cards.append(random.choice(cards))
  print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
  print("Win with a Blackjack 😎")
  ans=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
  if ans=='y':
    game()
  else:
    exit()
#The main function game  
def game():
  os.system('cls')
  print(art.logo)
  my_cards=[]
  for x in range(2):
    my_cards.append(random.choice(cards))
  your_score=sum(my_cards)
  print(f"   Your cards: {my_cards}, current score: {your_score}")
  computer_score=random.choice(cards)
  print(f"   Computer's first card: {computer_score}")
  if your_score==21:
    blackjack(my_cards,computer_score)
  else:
    another_card=input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card =='y':
      draw_more_cards(my_cards,computer_score)
    else:
      check_score(my_cards,computer_score)  

    
#Main    
ans=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if ans=='y':
  game()

