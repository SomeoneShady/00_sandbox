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
     player1 = deck[0:13]
     player2 = deck[14:26]
     player3 = deck[27:39]
     player4 = deck[40:52]
     print("""Player 1's hand will be {},"
    "Player 2's hand will be {}"
    "Player 3's hand will be {}"
    "And finally, Player 4's hand will be {}, happy card gaming!""".format(player1, player2, player3, player4))
elif num_of_players == 3:
    player1 = deck[0:18]
    player2 = deck[19:35]
    player3 = deck[36:52]
    print("""Player 1's hand will be {}
    Player 2's hand will be {}
    and Player 3's hand will be""".format(player1, player2, player3))
elif num_of_players == 2:
    player1 = deck[0:26]
    player2 = deck[27:52]
    print("""Player 1's hand will be {}
    Player 2's hand will be {}""".format(player1, player2))

