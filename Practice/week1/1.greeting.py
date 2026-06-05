def main():
    greeting()

    name = input("What's your name? ")
    greeting(name)
    

def greeting(to="World"):
    print(f"Hello {to}")


main()

