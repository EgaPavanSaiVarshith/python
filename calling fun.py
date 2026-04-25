def get_largest_sqr(list_x):  
    len_list = len(list_x)  
    for i in range(len_list):  
        x = list_x[i]
        list_x[i] = x * x
    largest = max(list_x)  
    return largest  

list_a = [1,-3,2]  
result = get_largest_sqr(list_a)  
print(result)
