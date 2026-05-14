fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
key=input()
n_key=input()
items=list(fruits.items())
copy=items.copy()
count=len(items)
for i in range(count):
    if items[i][0]==key:
        t=(n_key,items[i][1])
        copy[i]=t
print(copy)
