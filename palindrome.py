s = "LEVEL"
ans = ""
for i in range(len(s)-1,-1,-1):
    ans = ans + s[i]
if ans == s:
    print("It is a palindrome")
else:
    print("It is not a palindrome")