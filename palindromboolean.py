s = "KETTLE"
n = len(s)/2
mu = len(s)
valid =True
for i in range(int(n)):
    l = s[i]
    r = s[mu-2-i]
    print(l,r)
    if l != r:
        valid =False
        break
if valid:
        print("YES")
else:
        print("NO")