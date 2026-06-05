def main():
    # Take marks obtained
    marks_obt = int(input("Enter marks obtained: "))

    # Take total marks
    total_marks = int(input("Total marks possible: "))

    # Calc percentage
    print(f"Percentage: {percent_calc(marks_obt, total_marks):.2f}%")


def percent_calc(obt, total):

    return (obt / total) * 100


main()

