n=int(input())
fact=1 
for i in range(1,n+1):
    for j in range(1,i+1):
        fact=fact*j 
print(fact)
