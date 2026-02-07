s = "LEVEL"
n = 3
mu = n *2
valid =True
for i in range(n):
    l = s[i]
    r = s[mu-2-i]
    if l != r:
        valid =False
if valid:
        print("YES")
else:
        print("NO")