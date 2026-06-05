# take input 
# x = float(input("What's x? "))
# y = float(input("What's y? "))

#to round the addition and put commas as 1,000,000 using format string
# z= round(x+y)
# print(f"{z:,}")

#to round the division result to just 2 decimal places
# z = round(x/y, 2)
# print(z)

#to round the division result to just 2 decimal places using format string
# z = x/y
# print(f"{z:.2f}")


#CODE TO SQUARE A NUMBER
def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", square(x))

def square(n):
    # return n*n
    # return n**2
    return pow(n, 2)

main()