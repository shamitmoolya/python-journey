cost_list = [
        {"name": "Milk", "cost": 40},
        {"name": "Bread", "cost": 100},
        {"name": "Ghee", "cost": 80},
        {"name": "Butter", "cost": 120},
        {"name": "Soyabean", "cost": 80},
        {"name": "Wheat", "cost": 50}
    ]


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

