arr=[ 3,2,1,5,7,8,1,4,1,2,1,4,6 ]
ans=0
for i in range(len(arr)):
    if(arr[i]%3==0 and arr[i]%2==0):
        ans=ans+1
print(ans)
