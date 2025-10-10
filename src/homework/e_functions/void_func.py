
def display_payroll_check(gross_pay=100, fica_tax=7.65, federal_tax=8):
    net_pay = gross_pay - fica_tax - federal_tax
    print(f"Gross Pay:      {gross_pay:8.2f}")
    print(f"FICA:           {fica_tax:8.2f}")
    print(f"Federal Tax:    {federal_tax:8.2f}")
    print(f"Net Pay:        {net_pay:8.2f}")