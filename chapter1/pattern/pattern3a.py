s=int(input("Enter the number"))
p=1
for i in range(1,s+1):
    for j in range(1,i+1):
        print(p,end=" ")
        p+=1
    print(   )
    i+=1