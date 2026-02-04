arr=[ 4,6,8,3,21,5,7,8,2,5,6 ]
ans=0
for i in range(len(arr)):
    if(arr[i]%3==0 or arr[i]%2==0):
        ans=ans+1
print(ans)