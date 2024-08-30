numbers = [3, 0, 5, 0, 3]
new_numbers = []
not_zero = [i for i in numbers if i != 0]
len(numbers)
only_zero = [0] * (len(numbers) - len(not_zero))
list = not_zero + only_zero
print(len(numbers))
print(len(only_zero))
print(not_zero)
print(list)