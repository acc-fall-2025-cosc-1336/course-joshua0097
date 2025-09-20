from decisions import get_letter_grade

def main():
    grade = int(input("Enter your grade (0-100): "))
    letter_grade = get_letter_grade(grade)
    print(f"Your letter grade is: {letter_grade}")

if __name__ == "__main__":
    main()