# <<< Final >>>

# Function that runs all the previous code depending on its inputs
# (as a programmer copying the code multiple times pains me, I'm sorry)
def carpet_replacement_calculator(carpet_price, room_width, room_length, order_number):
    # Calculates the Room's Area
    room_area = room_width * room_length

    # Total Costs
    total_carpet_price = (carpet_price * room_area) * 1.2
    total_labor_cost = .75 * room_area
    total_tax = (total_carpet_price + total_labor_cost) * .07

    total_cost = total_carpet_price + total_labor_cost + total_tax

    # Print to Console
    print(f'Order #{order_number}')
    print(f'Room: {room_area} sq ft\nCarpet: ${total_carpet_price:.2f}\nLabor: ${total_labor_cost:.2f}')
    print(f'Tax: {total_tax:.2f}\nCost: ${total_cost:.2f}\n')

    # Return Total Cost
    return total_cost

# Order 1 <Inputs>
carpet_price1 = float(input('Input carpet price per square foot: '))
room_width1 = int(input('Input the room width in feet: '))
room_length1 = int(input('Input the room length in feet: '))

# Order 2 <Inputs>
carpet_price2 = float(input('Input carpet price per square foot: '))
room_width2 = int(input('Input the room width in feet: '))
room_length2 = int(input('Input the room length in feet: '))

# Order 3 <Inputs>
carpet_price3 = float(input('Input carpet price per square foot: '))
room_width3 = int(input('Input the room width in feet: '))
room_length3 = int(input('Input the room length in feet: '))

# Order 1 & Order 2 <Calculation> + Total Sales <Calculation + Print>
print(f'Total Sales: {carpet_replacement_calculator(carpet_price1, room_width1, room_length1, 1) + carpet_replacement_calculator(carpet_price2, room_width2, room_length2, 2) + carpet_replacement_calculator(carpet_price3, room_width3, room_length3, 3):.2f}')

# <<< Step 1 >>>

'''
# Inputs
carpet_price = float(input('Input carpet price per square foot: '))
room_width = int(input('Input the room width in feet: '))
room_length = int(input('Input the room length in feet: '))

# Calculates the Room's Area
room_area = room_width * room_length

# Total carpet price times plus an additional 20% for waste
total_carpet_price = (carpet_price * room_area) * 1.2

print(f'Room: {room_area} sq ft\nCarpet: ${total_carpet_price:.2f}')
'''

# <<< Step 2 >>>

'''
# Inputs
carpet_price = float(input('Input carpet price per square foot: '))
room_width = int(input('Input the room width in feet: '))
room_length = int(input('Input the room length in feet: '))

# Calculates the Room's Area
room_area = room_width * room_length

# Total Costs
total_carpet_price = (carpet_price * room_area) * 1.2
total_labor_cost = .75 * room_area

print(f'Room: {room_area} sq ft\nCarpet: ${total_carpet_price:.2f}\nLabor: ${total_labor_cost:.2f}')
'''

# <<< Step 3 >>>

'''
# Inputs
carpet_price = float(input('Input carpet price per square foot: '))
room_width = int(input('Input the room width in feet: '))
room_length = int(input('Input the room length in feet: '))

# Calculates the Room's Area
room_area = room_width * room_length

# Total Costs
total_carpet_price = (carpet_price * room_area) * 1.2
total_labor_cost = .75 * room_area
total_tax = (total_carpet_price + total_labor_cost) * .07

total_cost = total_carpet_price + total_labor_cost + total_tax

print(f'Room: {room_area} sq ft\nCarpet: ${total_carpet_price:.2f}\nLabor: ${total_labor_cost:.2f}')
print(f'Tax: {total_tax:.2f}\nCost: ${total_cost:.2f}')
'''

# <<< Step 4 >>>

'''
# Function that runs all the previous code depending on its inputs
# (as a programmer copying the code multiple times pains me, I'm sorry)
def carpet_replacement_calculator(carpet_price, room_width, room_length, order_number):
    # Calculates the Room's Area
    room_area = room_width * room_length

    # Total Costs
    total_carpet_price = (carpet_price * room_area) * 1.2
    total_labor_cost = .75 * room_area
    total_tax = (total_carpet_price + total_labor_cost) * .07

    total_cost = total_carpet_price + total_labor_cost + total_tax

    # Print to Console
    print(f'Order #{order_number}')
    print(f'Room: {room_area} sq ft\nCarpet: ${total_carpet_price:.2f}\nLabor: ${total_labor_cost:.2f}')
    print(f'Tax: {total_tax:.2f}\nCost: ${total_cost:.2f}\n')

    # Return Total Cost
    return total_cost

# Order 1 <Inputs>
carpet_price1 = float(input('Input carpet price per square foot: '))
room_width1 = int(input('Input the room width in feet: '))
room_length1 = int(input('Input the room length in feet: '))

# Order 2 <Inputs>
carpet_price2 = float(input('Input carpet price per square foot: '))
room_width2 = int(input('Input the room width in feet: '))
room_length2 = int(input('Input the room length in feet: '))

# Order 1 & Order 2 <Calculation> + Total Sales <Calculation + Print>
print(f'Total Sales: {carpet_replacement_calculator(carpet_price1, room_width1, room_length1, 1) + carpet_replacement_calculator(carpet_price2, room_width2, room_length2, 2):.2f}')
'''

# <<< Step 5 >>>

'''
# Function that runs all the previous code depending on its inputs
# (as a programmer copying the code multiple times pains me, I'm sorry)
def carpet_replacement_calculator(carpet_price, room_width, room_length, order_number):
    # Calculates the Room's Area
    room_area = room_width * room_length

    # Total Costs
    total_carpet_price = (carpet_price * room_area) * 1.2
    total_labor_cost = .75 * room_area
    total_tax = (total_carpet_price + total_labor_cost) * .07

    total_cost = total_carpet_price + total_labor_cost + total_tax

    # Print to Console
    print(f'Order #{order_number}')
    print(f'Room: {room_area} sq ft\nCarpet: ${total_carpet_price:.2f}\nLabor: ${total_labor_cost:.2f}')
    print(f'Tax: {total_tax:.2f}\nCost: ${total_cost:.2f}\n')

    # Return Total Cost
    return total_cost

# Order 1 <Inputs>
carpet_price1 = float(input('Input carpet price per square foot: '))
room_width1 = int(input('Input the room width in feet: '))
room_length1 = int(input('Input the room length in feet: '))

# Order 2 <Inputs>
carpet_price2 = float(input('Input carpet price per square foot: '))
room_width2 = int(input('Input the room width in feet: '))
room_length2 = int(input('Input the room length in feet: '))

# Order 3 <Inputs>
carpet_price3 = float(input('Input carpet price per square foot: '))
room_width3 = int(input('Input the room width in feet: '))
room_length3 = int(input('Input the room length in feet: '))

# Order 1 & Order 2 <Calculation> + Total Sales <Calculation + Print>
print(f'Total Sales: {carpet_replacement_calculator(carpet_price1, room_width1, room_length1, 1) + carpet_replacement_calculator(carpet_price2, room_width2, room_length2, 2) + carpet_replacement_calculator(carpet_price3, room_width3, room_length3, 3):.2f}')
'''