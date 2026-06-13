# We'll try writing data to the csv. We have originally just added :
# name,home
# in students1.csv 

# import csv

# name = input("What's your name: ")
# home = input("What's your home: ")

# with open("students1.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])


# To keep track of what is name and what's the home. 

import csv

name = input("What's your name: ")
home = input("What's your home: ")

with open("students1.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# fieldnames tells it what the heading of the column must be.

# If you had used writer.writerow({"home": home, "name": name}) the it would have written the same way as it has now.
