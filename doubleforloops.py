s ="one problem a day keeps the doctor away"
temp = 0
for i in range(len(s)):
    ch = s[i]
    if ch == " ":
        temp = temp + 1
print(temp+1)