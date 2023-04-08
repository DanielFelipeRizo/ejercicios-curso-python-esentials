c0=int(input("ingrese un entero positivo diferente de 0: "))
cont1=0
while c0>=0 and c0!=1:

    while c0%2==0 and c0!=1:
        c0=c0//2    
        print(c0)
        cont1=cont1+1
        break
    while c0%2!=0 and c0!=1:
        c0=3*c0+1
        print(c0)
        cont1=cont1+1
        break
    continue
print("numero de pasos: ",cont1)

#otra forma##############

c0 = int (input("Ingrese c0:"))

if c0 > 1:
    pasos = 0
    while c0 != 1:
        if c0 %2 != 0:
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2
        print(c0)
        c0 = cnew
        pasos += 1
        print("pasos =", pasos)
else:
        print("Valor de c0 incorrecto")
