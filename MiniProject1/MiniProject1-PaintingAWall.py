import math

# <<< Final >>>

# Inputs
wall_height = float(input('What is the Wall Height: '))
wall_width = float(input('What is the Wall Width: '))
cost_per_can = float(input('What is the cost per paint can: '))

# Calculations
wall_area = wall_height * wall_width
paint_needed = wall_area / 350.0
cans_needed = math.ceil(paint_needed)
paint_cost = cans_needed * cost_per_can
sales_tax = paint_cost * .07
total_cost = paint_cost + sales_tax

# Output to Console
print(f'Wall area: {wall_area:.1f} sq ft\nPaint needed: {paint_needed:.3f} gallons\nCans needed: {cans_needed} can(s)\nPaint cost: ${paint_cost:.2f}\nSales tax: ${sales_tax:.2f}\nTotal cost: ${total_cost:.2f}')

# <<< Step 1 >>>

'''
# Inputs
wall_height = float(input('What is the Wall Height: '))
wall_width = float(input('What is the Wall Width: '))
cost_per_can = float(input('What is the cost per paint can: '))

# Calculations
wall_area = wall_height * wall_width

# Output to Console
print(f'Wall area: {wall_area:.1f} sq ft')
'''

# <<< Step 2 >>>

'''
# Inputs
wall_height = float(input('What is the Wall Height: '))
wall_width = float(input('What is the Wall Width: '))
cost_per_can = float(input('What is the cost per paint can: '))

# Calculations
wall_area = wall_height * wall_width
paint_needed = wall_area / 350.0

# Output to Console
print(f'Wall area: {wall_area:.1f} sq ft\nPaint needed: {paint_needed:.3f} gallons')
'''

# <<< Step 3 >>>

'''
# Inputs
wall_height = float(input('What is the Wall Height: '))
wall_width = float(input('What is the Wall Width: '))
cost_per_can = float(input('What is the cost per paint can: '))

# Calculations
wall_area = wall_height * wall_width
paint_needed = wall_area / 350.0
cans_needed = math.ceil(paint_needed)

# Output to Console
print(f'Wall area: {wall_area:.1f} sq ft\nPaint needed: {paint_needed:.3f} gallons\nCans needed: {cans_needed} can(s)')
'''