# SHOWS = [
#     " avatar",
#     "avengers endgame ",
#     "wakanda Forever",
#     " d c universe"
# ]

# def main():
#     cleaned_show = []
#     for show in SHOWS:
#         cleaned_show.append(show.strip().title())

#     print(" ".join(cleaned_show))
#     # it adds " " instead of commas b/w the elements

# main()


# STRING SLICING:

def main():
    phone = "613-444-1000"

    # to get from 1st to 3rd element
    print(phone[:3])

    # to get from 8th to last element
    print(phone[8:])
    #more efficient:
    print(phone[-4:])


main()

