def calculate_percentage(number):
    
    # complete this function
    if (number<1000):
        value=((5/100)*number)
    else:
        value=((10/100)*number)
    return value


number = int(input())

result =calculate_percentage(number)#all the calculate_percentage function

print(result)
