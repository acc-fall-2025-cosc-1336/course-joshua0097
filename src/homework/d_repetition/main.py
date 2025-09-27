from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("\nHomework 4 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            num = input("Enter a number (1-9): ")
            if num.isdigit() and 1 <= int(num) < 10:
                print(f"Factorial of {num} is {get_factorial(int(num))}")
            else:
                print("Number must be an integer between 1 and 9.")
        elif choice == 2:
            num = input("Enter a number (1-99): ")
            if num.isdigit() and 1 <= int(num) < 100:
                print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(int(num))}")
            else:
                print("Number must be an integer between 1 and 99.")
        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()