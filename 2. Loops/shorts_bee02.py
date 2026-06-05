# WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# def main():
#     print("Welcome to Spelling Bee")
#     print("Your letters are: A I P C R H G")

#     while len(WORDS) > 0:
#         print(f"{len(WORDS)} words left!!")
#         guess = input("Guess: ")

#         if guess == "GRAPHIC":
#             WORDS.clear()
#             print("You've won.")

#         if guess in WORDS.keys():
#             points = WORDS.pop(guess)
#             # this will remove that key from the dictionary and return the value for that key in the dictionary.

#             print(f"Good Job ! You scored {points} points.")
            
#     print("That's the game.")

# main()



WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee")
    
    for word, point in WORDS.items():
# .items() gives us a set of key value pair i.e word contains the keys and point contains the values
        print(f"{word} was worth {point} points.")

main()

