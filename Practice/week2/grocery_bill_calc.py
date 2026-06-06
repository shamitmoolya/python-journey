prices = {
    "Milk": 40,
    "Bread": 100,
    "Ghee": 80,
    "Butter": 120,
    "Soyabean": 80,
    "Wheat": 50
}

def main():

    print("====Welcome to Shamit's Supermarket!!====")

    while True:
        try:
            item = input("Item: ")
            amount = prices[item]
        except KeyError:
            print(f"{item} isn't available in the supermarket.")
            print("Name something else !!")
        else:
            quantity = get_number("Quantity: ")
            break
    
    print("====BILL=====")
    print(f"Amount = {calculate_bill(amount, quantity)} rupees")
    print("Thanks a lot for shopping here!!")
    print("=============")
    

def calculate_bill(amount, quantity):
    return amount * quantity


def get_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Enter a valid quantity.")
        

main()




# OLD UNPOLISHED CODE: 
# cost_list = [
#         {"name": "Milk", "cost": 40},
#         {"name": "Bread", "cost": 100},
#         {"name": "Ghee", "cost": 80},
#         {"name": "Butter", "cost": 120},
#         {"name": "Soyabean", "cost": 80},
#         {"name": "Wheat", "cost": 50}
#     ]


# def main():
#     no_of_items = int(input("Enter the number of items you want to buy: "))

#     items = []

#     for _ in range(no_of_items):
#         items.append(input("Item name: ").strip().lower().title())

#     print("====BILL=====")
#     print(f"Total bill: {bill_calculator(items)} rupees.")
#     print("=============")


# def bill_calculator(items):
    
#     bill = 0

#     for item in items:
#         for cost in cost_list:
#             if item == cost["name"]:
#                 bill = bill + cost["cost"]
        
#     return bill


# main()

