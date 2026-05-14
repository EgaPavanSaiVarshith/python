num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
def string_to_int(list_a):
    new_list=[]
    for i in list_a:
        num=int(i)
        new_list.append(num)
    return new_list
num_list=input().split()
num_list=string_to_int(num_list)
set_a=set(num_list)
if num_set.issuperset(set_a):
    print("Superset")
elif num_set.issubset(set_a):
    print("Subset")
elif num_set.isdisjoint(set_a):
    print("Disjoint Set")
