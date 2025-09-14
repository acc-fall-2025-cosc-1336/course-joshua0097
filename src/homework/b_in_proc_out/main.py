from output import get_meal_amount, get_sales_tax_amount, get_tip_amount

tax_rate = 6.75 / 100  # 6.75% as a decimal
meal_amount = get_meal_amount()
tip_amount = get_tip_amount()

def main():
    sales_tax_amount = get_sales_tax_amount(meal_amount, tax_rate)
    total_bill = meal_amount + sales_tax_amount + tip_amount

    print(f"Meal Amount: ${meal_amount:.2f}")
    print(f"Sales Tax Amount: ${sales_tax_amount:.2f}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    
if __name__ == "__main__":
    main()