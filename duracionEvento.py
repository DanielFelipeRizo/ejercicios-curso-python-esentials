hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
minutosTermina=(min+dura)%60
sumaminutos=(min+dura)
horaTermina=(hora+(sumaminutos//60))%24

print("la hora de salida es: ",horaTermina,":",minutosTermina)
