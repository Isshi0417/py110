import random
import time

deck = [['S', 'A'], ['S', '2'], ['S', '3'], ['S', '4'], ['S', '5'], ['S', '6'],
        ['S', '7'], ['S', '8'], ['S', '9'], ['S', '10'], ['S', 'J'], ['S', 'Q'],
        ['S', 'K'],
        ['H', 'A'], ['H', '2'], ['H', '3'], ['H', '4'], ['H', '5'], ['H', '6'],
        ['H', '7'], ['H', '8'], ['H', '9'], ['H', '10'], ['H', 'J'], ['H', 'Q'],
        ['H', 'K'],
        ['C', 'A'], ['C', '2'], ['C', '3'], ['C', '4'], ['C', '5'], ['C', '6'],
        ['C', '7'], ['C', '8'], ['C', '9'], ['C', '10'], ['C', 'J'], ['C', 'Q'],
        ['C', 'K'],
        ['D', 'A'], ['D', '2'], ['D', '3'], ['D', '4'], ['D', '5'], ['D', '6'],
        ['D', '7'], ['D', '8'], ['D', '9'], ['D', '10'], ['D', 'J'], ['D', 'Q'],
        ['D', 'K']]
player = []
dealer = []

def play_game():
    # Shuffle the deck
    shuffle(deck)

    # Deal cards
    deal(deck)

    # Print hand
    print(f"Your hand: {player}.")
    print(f"Dealer: {dealer[0]} and an unknown card.")

    # Play and compare score
    who_wins(player_turn(player), dealer_turn(dealer))

# Decide winner
def who_wins(player_score, dealer_score):
    if player_score > dealer_score:
        prompt("You win!")
    else:
        prompt("Dealer wins!")

# Dealer turn
def dealer_turn(dealer):
    # Announce card
    prompt("Dealer reveals his hand:")
    print(dealer)

    dealer_score = total(dealer)

    # Hit if the difference between 21 and current number is greater than 5
    while (21 - dealer_score) > 5:
        time.sleep(3)
        prompt("Dealer hits!")
        dealer.append(deck.pop(0))
        prompt("Dealer's hand:")
        print(dealer)
        dealer_score = total(dealer)
        if busted(dealer_score):
            prompt("Dealer busted you win!")
            exit()
        else:
            prompt("Dealer stays!")
            break
    
    return dealer_score


# Player turn
def player_turn(player):
    player_score = total(player)
    while True:
        answer = input("=> Hit or Stay?")
        if answer == 'stay':
            break
        player.append(deck.pop(0))
        print(f"Your hand: {player}.")
        
        # Calculate the total
        player_score = total(player)
        print(f"=> You are at {player_score}.")

        if busted(player_score):
            break
    
    if busted(player_score):
        prompt("You busted!")
        prompt("Game over!")
        exit()
    else:
        prompt("You chose to stay!")

    return player_score

# Check if the score is busted
def busted(score):
    if score > 21:
        return True
    else:
        return False

# Calculate the total
def total(cards):
    values = [card[1] for card in cards]

    card_sum = 0
    for value in values:
        if value == "A":
            card_sum += 11
        elif value in ['J', 'Q', 'K']:
            card_sum += 10
        else:
            card_sum += int(value)

    aces = values.count("A")
    while card_sum > 21 and aces:
        card_sum -= 10
        aces -= 1

    return card_sum

# Deal the cards in alternating order
def deal(deck):
    for i in range(2):
        player.append(deck.pop(0))
        dealer.append(deck.pop(0))

# Shuffle the deck
def shuffle(deck):
    random.shuffle(deck)

# Prompt
def prompt(message):
    print(f"=> {message}")

play_game()