import random

cards = ["king", "queen", "jack"]

def main():

    # print(random.choice(cards))

    # print(random.choices(cards, k=2))
    # but it chooses with replacement

    # if you wanted without replacement:
    # print(random.sample(cards, k=2))

    # if you wanted some to have pre decided probability
    # print(random.choices(cards, weights=[100 , 0 , 0], k=2))
    # print(random.choices(cards, weights=[75 , 20 , 5], k=2))


    # if its too random then it'll be difficult to debug hence you can set a sedd that will always make a same random choice that will remain constant:
    random.seed(1)
    print(random.choices(cards, k=2))


main()