def main():
    pace = get_pace(miles = 16.3, minutes = 0)


def get_pace(miles, minutes):

    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0.")

    return minutes / miles

main()