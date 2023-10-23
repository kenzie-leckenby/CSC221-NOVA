# <<< Final >>>

# Inputs
wages = int(input('What is your income: '))
taxable_interest = int(input('Taxable interest: '))
unemployment_compensation = int(input('Unemployment compensation: '))
relationship_status = int(input('What is your relationship status: '))
taxes_withheld = int(input('Taxes  withheld: '))

# Calculations
agi = wages + taxable_interest + unemployment_compensation
deduction_amount = 12000 if relationship_status == 1 else 24000
taxable_income = agi - deduction_amount if (agi - deduction_amount >= 0) else 0

# Federal Tax Table
if relationship_status == 1:
    federal_tax = round(taxable_income * .1) if 0 <= taxable_income <= 10000 else 0
    federal_tax = round(1000 + (taxable_income-10000) * .12) if 10000 < taxable_income <= 40000 else federal_tax
    federal_tax = round(4600 + (taxable_income-40000) * .22) if 40000 < taxable_income <= 85000 else federal_tax
    federal_tax = round(14500 + (taxable_income-85000) * .24) if taxable_income > 85000 else federal_tax
else:
    federal_tax = round(taxable_income * .1) if 0 <= taxable_income <= 20000 else 0
    federal_tax = round(2000 + (taxable_income - 20000) * .12) if 20000 < taxable_income <= 80000 else federal_tax
    federal_tax = round(9200 + (taxable_income - 80000) * .22) if taxable_income > 80000 else federal_tax

tax_refund = abs(federal_tax - taxes_withheld) if (federal_tax - taxes_withheld) < 0 else 0

# Output to Console
if agi <= 120000:
    print(f'AGI: ${agi:,}\nDeduction: ${deduction_amount:,}\nTaxable income: ${taxable_income:,}\nFederal tax: ${federal_tax:,}\nTax refund: ${tax_refund:,}')
else:
    print(f'AGI: ${agi:,}')
    print('Error: Income too high to use this form')

# <<< Step 1 >>>

'''
# Inputs
wages = int(input('What is your income: '))
taxable_interest = int(input('Taxable interest: '))
unemployment_compensation = int(input('Unemployment compensation:'))
relationship_status = int(input('What is your relationship status: '))
taxes_withheld = int(input('Taxes  withheld: '))

# Calculations
agi = wages + taxable_interest + unemployment_compensation

# Output to Console
if agi <= 120000:
    print(f'AGI: ${agi}')
else:
    print(f'AGI: ${agi}')
    print('Error: Income too high to use this form')
'''

# <<< Step 2 >>>

'''
# Inputs
wages = int(input('What is your income: '))
taxable_interest = int(input('Taxable interest: '))
unemployment_compensation = int(input('Unemployment compensation: '))
relationship_status = int(input('What is your relationship status: '))
taxes_withheld = int(input('Taxes  withheld: '))

# Calculations
agi = wages + taxable_interest + unemployment_compensation
deduction_amount = 12000 if relationship_status == 1 else 24000
taxable_income = agi - deduction_amount if (agi - deduction_amount) >= 0 else 0

# Output to Console
if agi <= 120000:
    print(f'AGI: ${agi:,}\nDeduction: ${deduction_amount:,}\nTaxable income: ${taxable_income:,}')
else:
    print(f'AGI: ${agi:,}')
    print('Error: Income too high to use this form')
'''

# <<< Step 3 >>>

'''
# Inputs
wages = int(input('What is your income: '))
taxable_interest = int(input('Taxable interest: '))
unemployment_compensation = int(input('Unemployment compensation: '))
relationship_status = int(input('What is your relationship status: '))
taxes_withheld = int(input('Taxes  withheld: '))

# Calculations
agi = wages + taxable_interest + unemployment_compensation
deduction_amount = 12000 if relationship_status == 1 else 24000
taxable_income = agi - deduction_amount if (agi - deduction_amount >= 0) else 0

# Federal Tax Table
if relationship_status == 1:
    federal_tax = round(taxable_income * .1) if 0 <= taxable_income <= 10000 else 0
    federal_tax = round(1000 + (taxable_income-10000) * .12) if 10000 < taxable_income <= 40000 else federal_tax
    federal_tax = round(4600 + (taxable_income-40000) * .22) if 40000 < taxable_income <= 85000 else federal_tax
    federal_tax = round(14500 + (taxable_income-85000) * .24) if taxable_income > 85000 else federal_tax
else:
    federal_tax = round(taxable_income * .1) if 0 <= taxable_income <= 20000 else 0
    federal_tax = round(2000 + (taxable_income - 20000) * .12) if 20000 < taxable_income <= 80000 else federal_tax
    federal_tax = round(9200 + (taxable_income - 80000) * .22) if taxable_income > 80000 else federal_tax

# Output to Console
if agi <= 120000:
    print(f'AGI: ${agi:,}\nDeduction: ${deduction_amount:,}\nTaxable income: ${taxable_income:,}\nFederal Tax: ${federal_tax:,}')
else:
    print(f'AGI: ${agi:,}')
    print('Error: Income too high to use this form')
'''

