from value_return import get_gross_pay, get_fica_tax, get_federal_tax
from void_func import display_payroll_check

# Main program to calculate and display payroll check details
def main():
    try:
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter hourly pay rate: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours and rate.")
        return

    gross_pay = get_gross_pay(hours, rate)
    fica_tax = get_fica_tax(gross_pay)
    federal_tax = get_federal_tax(gross_pay)
    net_pay = gross_pay - (fica_tax + federal_tax)

    print(f"\nGross Pay:      {gross_pay:.2f}")
    print(f"FICA:           {fica_tax:.2f}")
    print(f"Federal Tax:    {federal_tax:.2f}")
    print(f"Net Pay:       {net_pay:.2f}")

print("\nDisplaying static payroll check:")
display_payroll_check()

if __name__ == "__main__":
    main()