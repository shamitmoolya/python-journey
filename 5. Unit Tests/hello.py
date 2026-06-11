# def main():
#     name = input("What's your name? ")
#     hello(name)

# def hello(to="World"):
#     print("hello, ", to)

# if __name__ == "__main__":
#     main()


# but look the hello function doesn't return anything but just gives a side effect of printing hello, name on the screen. Hence it can't be tested as square(). But as code becomes complex its good practice to avoid side effects for functions and instead return things. So we'll change this hello function by :

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="World"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
# now this hellop function is testable as pytest can test arguments and return values therefrom.