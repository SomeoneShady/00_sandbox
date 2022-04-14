from random import shuffle

def card_deck():

    suits = ["♥", "♦", "♣", "♠"]
    deck = []

    for item in suits:
        for x in range(1,14):
            if x == 11:
                deck.append("J" + item)
            elif x == 12:
                deck.append("Q" + item)
            elif x == 13:
                deck.append("K" + item)
            elif x == 1:
                deck.append("A" + item)
            else:
                deck.append(str(x) + item)
    return deck

def player_number(num_of_players):
    while True:
        try:
            response = int(input(num_of_players))
            break
        except ValueError:
            print("That number of players isn't possible! Try again!")
    return response


print("Welcome! Have you had trouble dealing with shuffling a deck of cards?")
print("Do you just want someone else to do it for you? Well step right up!")
print("We have just the thing for you! The Card Drawer 2001 (V2)!")
print("Just give us a moment and you'll have your cards in no time!")

deck = card_deck()
print(deck)
print("This is your deck, now, let's shuffle it and hand out some cards!")
shuffle(deck)


num_of_players = player_number("How many players am I drawing cards for?")
if num_of_players == 4:
    print(deck[0:13]
          deck[14:26]
          deck[27:39]
          deck[40:52])

