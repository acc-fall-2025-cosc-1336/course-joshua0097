# Global tax rates
FICA_TAX_RATE = 0.0765
FEDERAL_TAX_RATE = 0.08

def get_gross_pay(hours, rate):
    """
    Calculate gross pay, accounting for overtime (over 40 hours at 1.5x rate).
    """
    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate
    return gross_pay

def get_fica_tax(gross_pay):
    """
    Calculate FICA tax from gross pay using global FICA_TAX_RATE.
    """
    return gross_pay * FICA_TAX_RATE

def get_federal_tax(gross_pay):
    """
    Calculate federal tax from gross pay using global FEDERAL_TAX_RATE.
    """
    return gross_pay * FEDERAL_TAX_RATE