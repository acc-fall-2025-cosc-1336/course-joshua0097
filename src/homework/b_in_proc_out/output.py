def get_sales_tax_amount(meal_amount, tax_rate):
    return meal_amount * tax_rate

def get_meal_amount():
    return float(input("Enter the meal amount (as a decimal): "))

def get_tip_amount():
    return float(input("Enter the tip amount (as a decimal): "))