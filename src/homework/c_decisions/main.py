from decisions import get_letter_grade_if, get_letter_grade_switch

print("\nMAIN MENU\n")
print("1-Letter grade using if")
print("2-Letter grade using switch")
print("3-Exit\n")
option = input("Enter option: ")

def main():
    if option == "1":
        score = int(input("Enter score: "))
        grade = get_letter_grade_if(score)
        print(f"Letter grade (if): {grade}")
    elif option == "2":
        score = int(input("Enter score: "))
        grade = get_letter_grade_switch(score)
        print(f"Letter grade (switch): {grade}")
    elif option == "3":
        print("Exiting program.")
    else:
        print("Invalid option. Please try again.")
    
if __name__ == "__main__":
    main()