from output import get_sales_tax_amount, get_tip_amount

def main():
    meal_amount = float(input("Enter the meal amount (as a decimal): "))
    tip_rate = float(input("Enter the tip rate (as a decimal): "))
    tax_rate = 6.75 / 100  # 6.75% as a decimal

    sales_tax_amount = get_sales_tax_amount(meal_amount, tax_rate)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total_bill = meal_amount + sales_tax_amount + tip_amount

    print() # Print a blank line for better readability
    print(f"Meal Amount: ${meal_amount:.2f}")
    print(f"Sales Tax Amount: ${sales_tax_amount:.2f}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    
if __name__ == "__main__":
    main()