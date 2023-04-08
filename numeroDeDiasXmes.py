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

testYears = [1900, 2000, 2016, 1987,1400]
testMonths = [2, 2, 1, 11,4]
testResults = [28, 29, 31, 30,30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
