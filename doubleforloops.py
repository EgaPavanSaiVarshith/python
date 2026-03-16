li = [ 6 , 8 , 5 , 10 , 2]
for i in li:
    print(i,"Outside Loop")
    for j in li:
        print("Inside Loop")
    print(i,"Outside exiting")