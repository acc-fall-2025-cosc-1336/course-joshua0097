from value_return import get_gross_pay, get_fica_tax, get_federal_tax
from void_func import display_payroll_check

# Main program to calculate and display payroll check details
def main():
    print("Payroll Check Calculator") 
    print() # Blank line for better readability
    try:
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter hourly pay rate: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours and rate.")
        return

    gross_pay = get_gross_pay(hours, rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)

    print() # Blank line for better readability
    print("Payroll Check Details:")
    print() # Blank line for better readability
    display_payroll_check(gross_pay, fica_tax, federal_tax)

if __name__ == "__main__":
    main()