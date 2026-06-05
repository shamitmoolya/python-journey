name = input("What's your name? ").removeprefix

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermonie":
#     print("Griffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?") 


# if name == "Harry" or name == "Hermonie" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?") 


# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermonie":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")


match name:
    case "Harry" | "Hermonie" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


