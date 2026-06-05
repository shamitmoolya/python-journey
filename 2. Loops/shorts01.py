# Spacecraft dictionary
# def main():
#     spacecraft = {"name": "Voyager 1", "distance": 163}
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     =======REPORT=======

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ====================
#     """

# main()


# To declare a key value pair of distance outside the dictionay
# def main():
#     spacecraft = {"name": "Voyager 1"}
#     spacecraft["distance"] = 163
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     =======REPORT=======

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ====================
#     """

# main()


# Different condition
# def main():
#     spacecraft = {"name": "Voyager 1"}
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     =======REPORT=======

#     Name: {spacecraft.get("name", "Unknown")}
#     Distance: {spacecraft.get("distance", "Unknown")} AU

#     ====================
#     """

# main()
#Look in this case the distance keyword doesn't exist in the dictionary so if we had used :
#   Distance: {spacecraft["distance"]} AU
# Then it would be an error so we used :
#   Distance: {spacecraft.get("distance", "Unknown")} AU
# here it says that get the value of the key "distance" in the dictionary IF IT EXISTS. And if it doesn't then output "Unknown" there


# To add more than 1 keys-value pairs at once to a dictionary use update :
# def main():
#     spacecraft = {"name": "Voyager 1"}
#     spacecraft.update({"distance": 163, "orbit":"Sun"})
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     =======REPORT=======

#     Name: {spacecraft.get("name", "Unknown")}
#     Distance: {spacecraft.get("distance", "Unknown")} AU
#     Orbit: {spacecraft.get("orbit", "Unknown")}

#     ====================
#     """

# main()


# distances = {
#     "Voyager 1": 163,
#     "Pioneer": 142,
#     "James Webb Telescope": 42,
#     "Voyager 2": 154
# }

# for distance in distances:
#     print(f"{distance} has a distance of {distances[distance]} AU from Earth.")


# distances = {
#     "Voyager 1": 163,
#     "Pioneer": 142,
#     "James Webb Telescope": 42,
#     "Voyager 2": 154
# }

# for name in distances.keys():
#     print(f"{name} is at a distance of {distances[name]} AU from Earth.")
# .keys() gives keys of the dictionary


def main():
    distances = {
        "Voyager 1": 163,
        "Pioneer": 142,
        "James Webb Telescope": 42,
        "Voyager 2": 154
    }

    for distance in distances.values():
        print(f"{distance} AU is equal to {convert(distance)}m from Earth.")

def convert(distance):
    return distance * 143757707

main()
    # .values() gives values of the dictionary