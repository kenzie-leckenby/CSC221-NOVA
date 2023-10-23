import math

# <<< Final >>>

# Inputs
total_people = int(input('Total number of people: '))
average_slices = float(input('Average slices per person: '))
cost_per_pizza = float(input('Cost per pizza: '))

# Calculations
total_pizzas = math.ceil((total_people * average_slices)/8)
total_cost_pizzas = total_pizzas * cost_per_pizza
total_tax = total_cost_pizzas * .07
delivery_fee = (total_cost_pizzas + total_tax) * .2

print(f'Friday Night Party\n{total_pizzas} Pizzas: ${total_cost_pizzas:.2f}\nTax: ${total_tax:.2f}\nDelivery: ${delivery_fee:.2f}')





# <<< Step 1 >>>

'''
# Inputs
total_people = int(input('Total number of people: '))
average_slices = float(input('Average slices per person: '))
cost_per_pizza = float(input('Cost per pizza: '))

# Calculations
total_pizzas = math.ceil((total_people * average_slices)/8)
total_cost = total_pizzas * cost_per_pizza

print(f'Friday Night Party\n{total_pizzas} Pizzas: ${total_cost:.2f}')
'''

# <<< Step 2 >>>

'''
# Inputs
total_people = int(input('Total number of people: '))
average_slices = float(input('Average slices per person: '))
cost_per_pizza = float(input('Cost per pizza: '))

# Calculations
total_pizzas = math.ceil((total_people * average_slices)/8)
total_cost_pizzas = total_pizzas * cost_per_pizza
total_tax = total_cost_pizzas * .07
delivery_fee = (total_cost_pizzas + total_tax) * .2

print(f'Friday Night Party\n{total_pizzas} Pizzas: ${total_cost_pizzas:.2f}\nTax: ${total_tax:.2f}\nDelivery: ${delivery_fee:.2f}')
'''