# MODULES - libraries that were downloaded when we downloaded python hence they lie in you hard disk and so you can just call them using import

import random

# coin = random.choice(["heads", "tails"])
# print(coin)


# or you could have also done:
# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)


# number = random.randint(1, 10)
# print(number)
# this gives us a random number between 1 and 10 with 1 and 10 both inclusive.


# to take a list of values and shuffle them up:
cards = ["jack", "queen", "king"]
random.shuffle(cards)
# It shuffles the original cards list and doesn't return anything.
for card in cards:
    print(card)
