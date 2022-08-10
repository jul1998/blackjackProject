import random

#Create lists for compuer and pc cards



def dealCards ():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    card = random.choice(cards)
    return card
    



def detectBlackJack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return True
    else:
        return False


def score(cards):
    score = sum(cards)
    return score



def ifAceDrawn(cards):
    ace = 11
    if score(cards) > 21 and ace in cards:
        cards.remove(ace)
        cards.append(1)
    else:
        print("No ace was drawn")
        return sum(cards)


def add_cards(cards):
    cards.append(dealCards())








def user_get_cards(cards):
        
        add_cards(cards)
        return cards

def computer_get_cards(cards):
    while score(cards) < 16:
        print("Computer's turn")
        add_cards(cards)
    return cards

def compare(user_score, computer_score):
    if score(user_score) == score(computer_score):
        return "Draw 🙃"
    elif score(computer_score) == 0:
        return "Lose, opponent has Blackjack 😱"
    elif score(user_score) == 0:
        return "Win with a Blackjack 😎"
    elif score(user_score) > 21:
        return "You went over. You lose 😭"
    elif score(computer_score) > 21:
        return "Opponent went over. You win 😁"
    elif score(user_score) >score(computer_score):
        return "You win 😃"
    else:
        return "You lose 😤"
    

def game():
    game_over = False
    while not game_over:
        should_continue = input("You want restart? ").upper()
        if should_continue == "Y":
            global computer_cards
            global user_cards
            computer_cards = []
            user_cards = []
            ace = 11
            for card in range(0,2):
                user_cards.append(dealCards())
                computer_cards.append(dealCards())
                


            if detectBlackJack(computer_cards) or  detectBlackJack(user_cards):
                print("BlackJack")
                print(f"Your cards: {user_cards}. Current score: {score(user_cards)}")
                print(f"Computer cards: {computer_cards[0]}. Score: {score(computer_cards)}")
                break
            else:
                print(f"Your cards: {user_cards}. Current score: {score(user_cards)}")
                print(f"Computer cards: {computer_cards[0]}.")
                user_add = input("Do yo want to add more cards?").upper()
                if user_add == "Y":
                    
                    print(user_get_cards(user_cards))
                    
                print(computer_get_cards(computer_cards))

                if score(computer_cards) > 21 and ace in computer_cards:
                    computer_cards.remove(ace)
                    computer_cards.append(1)
                if score(user_cards) > 21 and ace in user_cards:
                    user_cards.remove(ace)
                    user_cards.append(1)

                print(compare(user_cards,computer_cards))
        else:
            game_over = True
game()

print(f"Your cards: {user_cards}. Current score: {score(user_cards)}")
print(f"Computer cards: {computer_cards[0]}. Score: {score(computer_cards)}")

