def string_to_int(str_num):
    new_list=[]
    for item in str_num:
        num=int(item)
        new_list.append(num)
    return new_list
str_num=input().split(",")
rotate=int(input())
int_list=string_to_int(str_num)
length=len(int_list)
rotate=rotate%length
first=int_list[:rotate]
second=int_list[rotate:]
second.extend(first)
print(second)
