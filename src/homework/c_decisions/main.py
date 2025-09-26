from decisions import get_options_ratio, get_faculty_rating

def main():
    options = int(input("Enter the number of options: "))
    total = float(input("Enter the total: "))
    ratio = get_options_ratio(options, total)
    rating = get_faculty_rating(ratio)
    print(f"Faculty rating: {rating}")

    
if __name__ == "__main__":
    main()