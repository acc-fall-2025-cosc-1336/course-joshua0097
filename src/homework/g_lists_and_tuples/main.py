from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("1-Show the list low /high values\n")
        print("2-Exit\n")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            values = []
            while True:
                val_str = input("Enter a list value (as integer):\n").strip()
                try:
                    val = int(val_str)
                except ValueError:
                    print("Invalid input, please enter an integer.")
                    continue
                values.append(val)

                if len(values) >= 3:
                    cont = input("Do you want to enter another value? (y/n) ").strip().lower()
                    if cont in ("n", "no"):
                        break
                    # if user enters yes/other, continue collecting
                # if fewer than 3 values, keep asking without the extra prompt

            low = get_lowest_list_value(values)
            high = get_highest_list_value(values)
            print(f"Lowest value: {low}")
            print(f"Highest value: {high}")

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid option, please choose 1 or 2.")

if __name__ == "__main__":
    main()