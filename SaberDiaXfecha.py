def isYearLeap(year):
    if year in[1600,1700,1800,1900,2000,2100,2200,2300,2400,2500]:
        if year%400==0:return True    
        else:return False       
    else:
        if year%4==0:return True   
        else:return False
        
def daysInMonth(year, month):
    if year < 1582 or month < 1 or month > 12: return None
    if isYearLeap(year)==True:
        if month in[1,3,5,7,8,10,12]:numDias=31
        elif month in[4,6,9,11]:numDias=30
        else:numDias=29        
    else:
        if month in[1,3,5,7,8,10,12]:numDias=31          
        elif month in[4,6,9,11]:numDias=30
        else:numDias=28
    return numDias

def dayOfYear(year, month, day):
    #coheficiente1
    a=None
    if year in range(1600,1699):a=7
    elif year in range(1700,1799):a=5
    elif year in range(1800,1899):a=3
    elif year in range(1900,1999):a=1
    elif year in range(2000,2099):a=0
    elif year in range(2100,2199):a=-2
    elif year in range(2200,2299):a=-4
    elif year in range(2300,2399):a=-6
    #coheficiente2
    b1=year%100
    b=b1+(b1//4)
    #coheficiente3
    if isYearLeap(year)==True:
        if month==1 or month==2:c=-1
    else: c=0
    #coheficiente4
    if month==1 or month==10:d=6
    elif month==2 or month==3 or month==11:d=2
    elif month==4 or month==7:d=5
    elif month==5:d=0
    elif month==6:d=3
    elif month==8:d=1
    elif month==9 or month==12:d=4
    #coheficiente5
    e=day

    total=(a+b+c+d+e)%7
    if total==1:total="Lunes"
    elif total==2:total="Martes"
    elif total==3:total="Miercoles"
    elif total==4:total="Jueves"
    elif total==5:total="Viernes"
    elif total==6:total="Sabado"
    else:total="Domingo"
    
    return total
print(dayOfYear(2021, 3, 12))
#anio,mes,dia

