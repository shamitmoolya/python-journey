# x = int(input("What's x? "))

# print(f"x is {x}.")


# ValueError - errors caused during runtime like if the user puts a string knowingly when asked for int.

# literal = something that is typed in.


# so use try except:

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}.")
# except ValueError:
#     print("x is not an integer.")


# its good practice to keep less code lines in try except 
# so we can push the print line out of try except block like below:

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer.")

# print(f"x is {x}.")

# but this will lead to a NameError as if the input is "cat" then 
# int(input("What's x? ")) will give a value error hence the except block will be executed but since print(f"x is {x}.") is outside the try except block, it has to be executed nonetheless. But since x is not assigned so it'll give a NameError. So use else: 


# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer.")
# else:
#     print(f"x is {x}.")

# I'll only execute else if i tried and succeeded.


# if the user puts a wrong value then to prompt for input again, we'll use infinite loop:


# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer.")
#     else:
#         break

# print(f"x is {x}")


# def main():
#     x = get_int()
#     print(f"x is {x}.")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer.")
#         else:
#             return x
    
# main()

# or look you dont require x , so:
# def main():
#     x = get_int()
#     print(f"x is {x}.")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer.")
            
# main()


# pass - what it does is that it catches that there is an error but it doesnt give any reply. It lets it pass and stays in the loop. Like :
def main():
    x = get_int()
    print(f"x is {x}.")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
            
main()


def main():
    x = get_int("What's x? ")
    print(f"x is {x}.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            
main()