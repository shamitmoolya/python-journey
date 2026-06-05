# LISTS
# students = ["Hermonie", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])


# students = ["Hermonie", "Harry", "Ron"]

# for student in students:
#     print(student)


# but if you want to iterate using numbers
# students = ["Hermonie", "Harry", "Ron"]

# for i in range(len(students)):
#     print(students[i])
# the range takes only numbers like 3 in the past cases. So here len(students) gives length of the list and passes it as an argument to range


#to give ranks as well in front of their names 
# students = ["Hermonie", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])


# DICT - Key value pairs
# students = {
#     "Hermonie": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
# }

# print(students["Hermonie"])
#Means go into the students dictionary and give me the value for the key Hermonie
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])


# students = {
#     "Hermonie": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
# }

# for student in students:
#     print(student)
# when iterating using a for loop in a dictionary then it'll iterate over the keys so you'll get hermonie harry ron draco. but it isn't useful as we wanted the houses and not their names.


# students = {
#     "Hermonie": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep=", ")
# students[student] means it'll go to hermonie's location and get back her house

#Output:
# Hermonie, Gryffindor
# Harry, Gryffindor
# Ron, Gryffindor
# Draco, Slytherin


# a list of dictionaries i.e. each student is itself a dictionary
students = [
    {"name": "Hermonie", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
# None - a special keyword means non existence of a value.

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

