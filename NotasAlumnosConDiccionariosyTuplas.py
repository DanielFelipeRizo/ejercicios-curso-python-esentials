grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] = grupo[nombre] + (calif,)
    else:
        grupo[nombre] = (calif,)
        
for n in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for c in grupo[n]:
        sum += c
        contador += 1
    print(n, ":", sum / contador)
