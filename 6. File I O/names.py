# names = []

# for _ in range(3):
#     names.append(input("What's your name: "))

# for name in sorted(names):
#     print(f"hello, {name}")


# name = input("What's your name: ")

# open = programmers technique to open a file 
# file = open("names.txt", "w")
# "w" = means i am going to write into file names.txt. 

# file.write(name)
# file.close()

# But whenever we run the python names.py "w" will recreate the names.txt hence erasing he earlier data. So we should have appended the words 


# name = input("What's your name: ")

# file = open("names.txt", "a")
# file.write(name)
# file.close()
# "a" = means to append onto the file 

#But it'll give us HermonieHarryRon.
# write itself doesn't add "\n" like print.
# rm names.txt = to remove the current file


# but no need to close the file as you can use with keyword instead. All in the indentated block will be done and it will automatically close the file thereafter.
# name = input("What's your name: ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# To read all the data in names.txt :
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line)

# But OUTPUT:
# hello, Hermonie

# hello, Harry

# hello, Ron

# hello, Draco

# This extra space is due to the \n already in the line and the \n that print adds itself, so you can remove it by rstrip().


# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())


# BUt you can better the code by:
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())
# But if i have to sort then i can't go line by line.

# open("names.txt") is enough to read a file. No need to specify "r" explicitly.


# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())
# but when we want to do some changes to data in a file, its advisible to use a list or something to store data and then sort or do what you want over it so we will do:


# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")


# Instead of sorting from a to z if we wan to sort from z to a:
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
