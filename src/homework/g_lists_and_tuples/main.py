from lists import get_p_distance_matrix


def main():
    while True:
        print("\n1-Get p distance matrix")
        print("2-Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            sequences = []
            print("Enter DNA sequences (one per line, empty line to finish):")
            while True:
                seq = input().strip()
                if not seq:
                    break
                sequences.append(seq)
            if sequences:
                result = get_p_distance_matrix(sequences)
                print(result)
            else:
                print("No sequences entered.")
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()