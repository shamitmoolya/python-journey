def main():
    while True:
        obt = int(input("Marks obtained: "))
        if obt >= 0:
            break

    while True:
        total = int(input("Total Marks: "))
        if total >= 0:
            break
    
    print(f"The Grade is {student_grade(obt, total):.2f}%")


def student_grade(obtained, total):
    return (float)(obtained / total) * 100

main()
