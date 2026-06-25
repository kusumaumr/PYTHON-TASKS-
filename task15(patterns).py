#1)Square Pattern
n=4
m=4
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()
#2)Right Triangle
n=4
for i in range(n):
    for j in range(i+1):
        if(i+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#3)Number Triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#4)Repeated Number Triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#5)Alphabet Triangle
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
#6)Inverted Star Triangle 
n=3
for i in range(n,-1,-1):
    for j in range(i+1):
        if(i+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#7)Inverted Number Triangle
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#8)Continuous Number Pattern
num=1   
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
#9)Right-Aligned Star Triangle    
n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for i in range(i):
        print("*", end="")
    print()
#10)Pyramid Pattern
n=6
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i+1):
        # if(j==0 or i==n-1 or j==0):
        #     print("*", end=" ")
        # else:
        #     print(" ",end=" ")  
        print("*",end=" ")
    print()