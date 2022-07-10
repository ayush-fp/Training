def fifthPowerDigitSum(num):
    sum = 0
    for x in str(num):
        sum = sum + int(x)**5
    return sum

def fun():
    sum = 0
    for i in range(2, 1000000):
        if (i == fifthPowerDigitSum(i)):
            sum = sum + i
	
    return sum
    
print("\nSum : ", fun())