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

c=3
for i in range(c):
    temp = 3
    if i==0:
        temp=3
    if i==1:
        temp=2
    if i==2:
        temp=1
    for j in range(temp):
        print("*",end = "")
    print()