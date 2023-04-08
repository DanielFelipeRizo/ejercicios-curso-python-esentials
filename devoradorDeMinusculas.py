userWord = input("Ingresa tu palabra:")
userWord = userWord.upper ()
for letter in userWord:
    if letter=="A":
        continue
    elif letter=="E":
        continue
    elif letter=="I":
        continue   
    elif letter=="O":
        continue
    elif letter=="U":
        continue  
    else:
        print(letter, end="")
        
#otra forma##########
userword=(input("Ingrese una palabra: ")).upper()
#userword=(input("Ingrese una palabra: ")).lower()
for letra in userword:
	if letra in ("A","E","I","O","U"):
	    continue
	print(letra,end="")

        
