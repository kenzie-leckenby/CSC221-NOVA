import math

# <<< Final >>>

# Pizza Total Cost Calculator
def pizza_calculator(day, total_people, average_slices, cost_per_pizza):
    # Calculations
    total_pizzas = math.ceil((total_people * average_slices)/8)
    total_cost_pizzas = total_pizzas * cost_per_pizza
    total_tax = total_cost_pizzas * .07
    delivery_fee = (total_cost_pizzas + total_tax) * .2
    total_cost = total_cost_pizzas + total_tax + delivery_fee

    # Print to Console
    print(f'{day} Night Party\n{total_pizzas} Pizzas: ${total_cost_pizzas:.2f}\nTax: ${total_tax:.2f}\nDelivery: ${delivery_fee:.2f}\nTotal: ${total_cost:.2f}\n')
    return total_cost

# Friday Night <Inputs>
total_people1 = int(input('Total number of people Friday: '))
average_slices1 = float(input('Average slices per person Friday: '))
cost_per_pizza1 = float(input('Cost per pizza Friday: '))
# Saturday Night <Inputs>
total_people2 = int(input('Total number of people Saturday: '))
average_slices2 = float(input('Average slices per person Saturday: '))
cost_per_pizza2 = float(input('Cost per pizza Saturday: '))
# Sunday Night <Inputs>
total_people3 = int(input('Total number of people Sunday: '))
average_slices3 = float(input('Average slices per person Sunday: '))
cost_per_pizza3 = float(input('Cost per pizza Sunday: '))

# Friday and Saturday Night <Calculations + Print>
print(f'Weekend Total: ${(pizza_calculator("Friday", total_people1, average_slices1, cost_per_pizza1) + pizza_calculator("Saturday", total_people2, average_slices2, cost_per_pizza2) + pizza_calculator("Sunday", total_people3, average_slices3, cost_per_pizza3)):.2f}')


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

# <<< Step 3 >>>

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
total_cost = total_cost_pizzas + total_tax + delivery_fee

# Print to Console
print(f'Friday Night Party\n{total_pizzas} Pizzas: ${total_cost_pizzas:.2f}\nTax: ${total_tax:.2f}\nDelivery: ${delivery_fee:.2f}\nTotal: ${total_cost:.2f}')
'''

# <<< Step 4 >>>

'''
# Pizza Total Cost Calculator
def pizza_calculator(day, total_people, average_slices, cost_per_pizza):
    # Calculations
    total_pizzas = math.ceil((total_people * average_slices)/8)
    total_cost_pizzas = total_pizzas * cost_per_pizza
    total_tax = total_cost_pizzas * .07
    delivery_fee = (total_cost_pizzas + total_tax) * .2
    total_cost = total_cost_pizzas + total_tax + delivery_fee

    # Print to Console
    print(f'{day} Night Party\n{total_pizzas} Pizzas: ${total_cost_pizzas:.2f}\nTax: ${total_tax:.2f}\nDelivery: ${delivery_fee:.2f}\nTotal: ${total_cost:.2f}\n')
    return total_cost

# Friday Night <Inputs>
total_people1 = int(input('Total number of people: '))
average_slices1 = float(input('Average slices per person: '))
cost_per_pizza1 = float(input('Cost per pizza: '))
# Saturday Night <Inputs>
total_people2 = int(input('Total number of people: '))
average_slices2 = float(input('Average slices per person: '))
cost_per_pizza2 = float(input('Cost per pizza: '))

# Friday and Saturday Night <Calculations + Print>
print(f'Weekend Total: ${(pizza_calculator("Friday", total_people1, average_slices1, cost_per_pizza1) + pizza_calculator("Saturday", total_people2, average_slices2, cost_per_pizza2)):.2f}')
'''