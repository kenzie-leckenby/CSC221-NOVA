# <<< Final >>>

# Assuming inputs are either floats or integers
class ListProperties():
    def __init__(self, input_list):
        self.input_list = input_list

    def minimum(self):
        return float(min(self.input_list))

    def maximum(self):
        return float(max(self.input_list))

    def mean(self):
        return float(sum(self.input_list)/len(self.input_list))

    def palindrome(self):
        return True if self.input_list == self.input_list[::-1] else False

    def median(self):
        sorted_list = sorted(self.input_list)
        return sorted_list[len(sorted_list)//2] if len(sorted_list) % 2 != 0 else (sorted_list[(len(sorted_list)//2)-1] + sorted_list[(len(sorted_list)//2)])/2

    def mode(self):
        sorted_list = sorted(self.input_list)
        most_occurences = 0
        for element in sorted_list:
            most_occurences =  element if sorted_list.count(element) > sorted_list.count(most_occurences) else most_occurences
        return most_occurences

input_list = input('Input a list (seperate each element with a space): ').split()
print()

for i in range(len(input_list)):
    input_list[i] = float(input_list[i])

input_list = ListProperties(input_list)

print(f'Minimum Value: {input_list.minimum():.2f}\nMaximum Value: {input_list.maximum():.2f}')
print(f'Mean Value: {input_list.mean():.2f}')
print(f'Palidrome: {input_list.palindrome()}')
print(f'Median: {input_list.median():.2f}')
print(f'Mode: {input_list.mode():.2f}')


# <<< Step 1 >>>

'''
# Assuming inputs are either floats or integers
class ListProperties():
    def __init__(self, input_list):
        self.input_list = input_list

    def minimum(self):
        return min(self.input_list)

    def maximum(self):
        return max(self.input_list)

input_list = input('Input a list (seperate each element with a space): ').split()
print()

input_list = ListProperties(input_list)

print(f'Minimum Value: {input_list.minimum()}\nMaximum Value: {input_list.maximum()}')
'''

# <<< Step 2 >>>

'''
# Assuming inputs are either floats or integers
class ListProperties():
    def __init__(self, input_list):
        self.input_list = input_list

    def minimum(self):
        return float(min(self.input_list))

    def maximum(self):
        return float(max(self.input_list))

    def mean(self):
        return float(sum(self.input_list)/len(self.input_list))

input_list = input('Input a list (seperate each element with a space): ').split()
print()

for i in range(len(input_list)):
    input_list[i] = float(input_list[i])

input_list = ListProperties(input_list)

print(f'Minimum Value: {input_list.minimum():.2f}\nMaximum Value: {input_list.maximum():.2f}')
print(f'Mean Value: {input_list.mean():.2f}')
'''

# <<< Step 3 >>>

'''
# Assuming inputs are either floats or integers
class ListProperties():
    def __init__(self, input_list):
        self.input_list = input_list

    def minimum(self):
        return float(min(self.input_list))

    def maximum(self):
        return float(max(self.input_list))

    def mean(self):
        return float(sum(self.input_list)/len(self.input_list))

    def palindrome(self):
        return True if self.input_list == self.input_list[::-1] else False

input_list = input('Input a list (seperate each element with a space): ').split()
print()

for i in range(len(input_list)):
    input_list[i] = float(input_list[i])

input_list = ListProperties(input_list)

print(f'Minimum Value: {input_list.minimum():.2f}\nMaximum Value: {input_list.maximum():.2f}')
print(f'Mean Value: {input_list.mean():.2f}')
print(f'Palidrome: {input_list.palindrome()}')
'''

# <<< Step 4 >>>

'''
# Assuming inputs are either floats or integers
class ListProperties():
    def __init__(self, input_list):
        self.input_list = input_list

    def minimum(self):
        return float(min(self.input_list))

    def maximum(self):
        return float(max(self.input_list))

    def mean(self):
        return float(sum(self.input_list)/len(self.input_list))

    def palindrome(self):
        return True if self.input_list == self.input_list[::-1] else False

    def median(self):
        sorted_list = sorted(self.input_list)
        return sorted_list[len(sorted_list)//2] if len(sorted_list) % 2 != 0 else (sorted_list[(len(sorted_list)//2)-1] + sorted_list[(len(sorted_list)//2)])/2

input_list = input('Input a list (seperate each element with a space): ').split()
print()

for i in range(len(input_list)):
    input_list[i] = float(input_list[i])

input_list = ListProperties(input_list)

print(f'Minimum Value: {input_list.minimum():.2f}\nMaximum Value: {input_list.maximum():.2f}')
print(f'Mean Value: {input_list.mean():.2f}')
print(f'Palidrome: {input_list.palindrome()}')
print(f'Median: {input_list.median():.2f}')
'''