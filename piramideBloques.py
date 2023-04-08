bloques = int(input("Ingrese el número de bloques: "))
capas=0
cont=0
# Escribe tu código aquí.
while bloques>1:
    capas=capas+1
    bloques=bloques-capas
    if bloques>=0:
        cont=cont+1      
print("la altura es: ",cont)

#otra forma#########
bloques = int (input("Ingrese el número de bloques:"))

altura = 0
encapa = 1
while encapa <= bloques:
	altura += 1
	bloques -= encapa
	encapa += 1
print("La altura de la pirámide:", altura)
