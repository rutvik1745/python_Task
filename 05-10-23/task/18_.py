row = 5
for i in range(row+1):
    for j in range(i):
        print("*",end=" ")
       
    print()
for i in range(row,1,-1):
    for j in range(i-1):
        print("*",end=" ")
       
    print()



