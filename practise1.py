# # # # # print("Hello",end = "\n")
# # # # #  print("Pavan")

# # # # print("Hello",end = " 1 ")
# # # # print("Pavan",end = " 2 ")
# # # # print("Boom Boom",end=" Bumrah ")

# # # li = ["hello","pavan","boom"]
# # # for i in range(len(li)):
# # #     print(li[i],end = " ")

# # r=5
# # c=5
# # for i in range(r):
# #     for j in range(c):
# #         print("*",end= " ")
# #     print()

r=5
c=5
# for i in range(r):
#     for j in range(c):
#         print("*",end= "")
#         if j!=c-1:
#             print("-",end="")
#     print()

# r=3
# c=10
# for i in range(r):
#     for j in range(c):
#         print("*",end= "")
#         if j!=c-1:
#             print("-",end="")
#     print()

r=10
c=3
# for i in range(r):
#     for j in range(c):
#         print("*",end= "")
#         if j!=c-1:
#             print("-",end="")
#     print()

# r=10
# c=3
# for i in range(r):
#     for j in range(c):
#         print("*",end= "")
#         if j!=c-1:
#             print(" ",end="")
#     print()

# r=5
# c=5
# for i in range(r):
#     for j in range(c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#         # if j!=c-1:
#         #     print(" ",end="")
# #     print()

# r=4
# c=15
# for i in range(r):
#     for j in range(c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             print("*",end = "")
#         else:
#             print(" ",end = "")
#         if j!=c-1:
#             print(" ",end="")
#     print()

# c=3
# for i in range(c):
#     temp = 3
#     if i==0:
#         temp=c - 0
#     if i==1:
#         temp=c - 1
#     if i==2:
#         temp=c - 2
#     for j in range(temp):
#         print("*",end = "")
#     print()

# c=3
# for i in range(c):
#     temp = c - i
#     for j in range(temp):
#         print("*",end = "")
#     print()

# r=6
# c = 3
# c1 = r-1
# for i in range(r):
#     for j in range(c1-i):
#         print("*",end = "")
#     for k in range(3):
#          print("-",end="")
#     print()

# r=6
# c = 3
# c1 = r-1
# for i in range(r):
#     for j in range(c1-i):
#         print(" ",end = "")
#     for k in range(c):
#          print("*",end="")
#     print()

# r=6
# c = 3
# c1 = r-1
# for i in range(r):
#     for j in range(i):
#         print("*",end = "")
#     for k in range(c):
#          print("*",end="")
#     print()

# c=9
# for i in range(c):
#     temp=c-i
#     for j in range(temp):
#         print("*",end="")
#     print()

# r=3
# n=r-1
# for i in range(r):
#     for j in range(n-i):
#         print("-",end="")
#     print("Hello",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("-",end="")
#     print()

# r=5
# n=r-1
# for i in range(r):
#     for j in range(n-i):
#         print(" ",end="")
#     temp = i * 2 + 1 
#     for k in range(temp):
#             print("*",end="")
#     print()

r=5
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(2*r-1-(2*i)):
            print("*",end="")
    print()