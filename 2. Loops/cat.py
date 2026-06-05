# print("Meow")
# print("Meow")
# print("Meow")

#WHILE

# i = 3
# while i != 0:
#     print("Meow")
#     i = i - 1


# i = 1
# while i <= 3:
#     print("Meow")
#     i = i + 1


# i = 0
# while i < 3:
#     print("Meow")
#     i += 1
    # i++ and i-- doesn't act in python



#FOR

# for i in [0, 1, 2]:
#     print("meow")


# for i in range(10):
#     print("meow")
# but since i is not useful since i itself is not needed so use _ 


# for _ in range(10):
#     print("meow")



# ANOTHER WAY but not advsible but can be done in python
# print("meow\n" * 3, end="")



# n = int(input("What's n? "))
# but the user can even put a negative number above which we dont want so

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n
 

def meow(n):
    for _ in range(n):
        print("meow")

main()

 