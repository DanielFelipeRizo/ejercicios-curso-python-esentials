def isYearLeap(year):
    if year in[1600,1700,1800,1900,2000,2100,2200,2300,2400,2500]:
        if year%400==0:
            return True
        else:
            return False
        
    else:
        if year%4==0:
            return True
        else:
            return False
        

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
