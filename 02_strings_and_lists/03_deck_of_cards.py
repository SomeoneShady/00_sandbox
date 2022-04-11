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


print("Welcome! Have you had trouble dealing with shuffling a deck of cards?")
print("Do you just want someone else to do it for you? Well step right up!")
print("We have just the thing for you! The Card Drawer 2001 (V2)!")
print("Just give us a moment and you'll have you cards in no time!")
