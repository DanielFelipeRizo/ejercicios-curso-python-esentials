def isPrime(num):
    cont=0
    co=0
    for i in range(2,num):
        if num%i != 0:cont=cont+1
           
    for i in range(2,num):co=co+1
        
    if cont==co:return True
        
    else: return False

for i in range(1, 100):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
