from strings import get_hamming_distance, get_dna_complement
def main():
    while True:
        print("1-Hamming Distance\n\n2-Dna Complement\n\n3-Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            s1 = input("Enter first string: ")
            s2 = input("Enter second string: ")
            try:
                result = get_hamming_distance(s1, s2)
            except Exception as e:
                print(f"Error: {e}")
            else:
                print(result)
        elif choice == "2":
            s = input("Enter a DNA string: ")
            try:
                result = get_dna_complement(s)
            except Exception as e:
                print(f"Error: {e}")
            else:
                print(result)
        elif choice == "3":
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()