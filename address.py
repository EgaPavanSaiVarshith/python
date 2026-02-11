s="1.1.1"
ans =""
for i in range(len(s)):
    ch = s[i]
    if ch == ".":
        ans = ans + "[.]"
    else:
        ans = ans + ch
print(ans)
    