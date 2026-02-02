a = [123, 456, 789]
res = [sum(int(digit) for digit in str(val)) for val in a]
print(res)