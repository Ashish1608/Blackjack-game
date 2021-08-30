import random
from art import logo
from os import system

cls = lambda: system('cls')

def deal_card():
    """ Takes the deck of cards and draws the random card out of it """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards dealt and returns the score calculated from the cards. 
       It also changes the value of 'Ace' to '1' from '11' 
       if score with 'Ace' is greater than 21 and then re-calculates the score""" 

    score = sum(cards)
    num_of_cards = len(cards)

    if (score == 21) and (num_of_cards == 2) :
        return 0                                       # here '0' is used to represent the BlackJack condition in our game
    if (11 in cards) and score > 21:
        cards.remove(11)
        cards.append(1)

    return score

def compare(user_score, computer_score) :
    """compares the scores of user and computer"""
    if (user_score > 21) and (computer_score > 21):
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card()) 

    while not is_game_over:                                                   # The score will need to be re-checked with every new card dealt to user
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:                        # after user stops playing , computer will continue
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))

# Ask the user if they want to restart the game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    cls()
    play_game()