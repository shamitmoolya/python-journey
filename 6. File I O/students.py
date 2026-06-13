# TO store related values like :

# Hermonie,Gryffindor
# Harry,Gryffindor
# Ron,Gryffindor
# Draco,Slytherin

# we'll use .csv (COMMA SEPARATED VALUES) files to stored realted values separated by commas.



# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# split(",") - will return us the list of items separated by commas. But instead of taking the list "row", as we already know that split in this case will return just 2 values so just take them in 2 variables i.e. "name" & "house"



# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")



# But if we want to sort the output based on the name, just like we did in names.py:

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# Even though this is working but this is sloppy as instead of sortiung by names, we are sorting using whole english sentences and we are lucky that the name came in start of sentence but what if it doesn't. So its better to sort by student's names.



# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# But in this the names aren't sorted yet.

# Notice that in student['name'], name is in single quotes as double quotes can't be used in double quotes of print so to let python differentiate.

# Point : Instead of :

        # student = {}
        # student["name"] = name
        # student["house"] = house

# we can simply do:

        # student = {"name": name, "house": house}

# it'll have the same effect.



# To sort them you can't just do:
# for student in sorted(students): 
# as the list doesn't just have names now. It has a dictionary in it.



# So we'll have to tell the program to go to the "name" key in student dictionary in list "students", we'll do it as below:

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# So what happens in sorted(students, key=get_name) is to sort the students list on the return value of get_name function which is student["name"].



# If you want to sort from z to a instead of a to z:

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")



# To sort using house name reversed:
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")



# Going back to the code for sorting using name, we can write it in even better way as :

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# The key=lambda student: student["name"] is equivalent to the key=get_name we used earlier. The get_name function was just to return student["name"] and no other use hence we could exclude the get_name function entirely by using an anonymous function "lambda" which takes each student dictionary as the argument and returns student["name"] to the key.



# students.csv initial data:

# Hermonie,Gryffindor
# Harry,Gryffindor
# Ron,Gryffindor
# Draco,Slytherin

# We'll change it here to:

# Harry,"Number Four, Privet Drive"
# Ron,The Burrow
# Draco,Malfoy Manor



# But what if the text in studwnts.csv itself hs a comma then how will you deal with it. 

# Actually you can use the csv library.

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")



# Upon adding name,home as the first line in students.csv 

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

# csv.reader(file) iterates one by one top to bottom and returns a list for each row.
# But csv.DictReader(file) iterates similarly and returns a dictionary.


# But now even if you interchange the position of each column like:

# home,name
# "Number Four, Privet Drive",Harry
# The Burrow,Ron
# Malfoy Manor,Draco

#  then still it will know which is name and which is home.



# Even if you add house column too but use the same code then still it'll work thats the use of DictReader 