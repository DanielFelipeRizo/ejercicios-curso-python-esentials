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
    for i in range(1,month):
        totalDias=daysInMonth(year, month)*month
    
    return totalDias
print(dayOfYear(2002, 2, 10))
#print(daysInMonth(2000,2))
#anio,mes,dia
