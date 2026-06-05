# cost_list = {
#     "Milk": 40,
#     "Bread": 100,
#     "Ghee": 80,
#     "Butter": 120,
#     "Soyabean": 80,
#     "Wheat": 50
# }

# def main():
    
#     items = []

#     print("===BILL===")

#     for things, cost in cost_list.items():
#         for item in items:
#             while item == things: 
#                 items.append(input("Item: ").strip().lower().title())

    

#     print(items)



cost_list = {
    "Milk": 40,
    "Bread": 100,
    "Ghee": 80,
    "Butter": 120,
    "Soyabean": 80,
    "Wheat": 50
}


def main():
    no_of_items = int(input("Enter the number of items you want to buy: "))

    items = []

    for _ in range(no_of_items):
        items.append(input("Item name: ").strip().lower().title())

    print("====BILL=====")
    print(f"Total bill: {bill_calculator(items)} rupees.")
    print("=============")


def bill_calculator(items):
    
    bill = 0

    for item in items:
        for cost in cost_list:
            if item == cost["name"]:
                bill = bill + cost["cost"]
        
    return bill


main()




    






            
# def bill_calc(items, quans):

#     bill = 0

#     for cost in cost_list.values():
#         for item in items:
#             for quan in quans:




main()