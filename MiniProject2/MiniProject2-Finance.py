# Using annual interest to avoid messy float division which soon gets muddy
def future_investment_value(investment_amount, annual_interest, years):
    return round(investment_amount * (1+annual_interest)**(years))

# Inputs
user_investment_amount = int(input('Investment Amount: '))
user_monthly_interest = (int(input('Annual Interest Rate: '))/100)

# Prints the years for the top banner
for row in range(0, 2):
    # Prints the years then the investment value based on the years
    for year in range(1, 21):
        print(f'{f"Year {year}:":^12}', end='') if row == 0 else print(f'{f"${future_investment_value(user_investment_amount, user_monthly_interest, year):,}":^12}', end='')
    print()

