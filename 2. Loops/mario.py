# print("#")
# print("#")
# print("#")


# for _ in range(3):
#     print("#")


# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()


# def main():
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")

# main()


# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()


#for a 3 * 3 square
# def main():
#     print_square(3)

# def print_square(size):

#     #for each row in square
#     for i in range(size):

#         # for each brick in row
#         for j in range(size):

#             #print brick
#             print("#", end="")
        
#         print()

# main()


#other way for it without the inner loop
# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#             print("#" * size)

# main()


#another way
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
            print_row(size)

def print_row(width):
     print("#" * width)

main()


