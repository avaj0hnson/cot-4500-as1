import numpy as np 

def doublePrecision(binaryNum):
    # Question 1
    correctedBinaryNum = binaryNum.ljust(64, '0')
    sign = binaryNum[0]
    exp = 0
    mantisa = 0
    
    for i in range(1, 12):
        if correctedBinaryNum[i] == '1':
            exp += 2**(11 - i)
    
    for i in range(12, len(correctedBinaryNum)):
        if correctedBinaryNum[i] == '1':
            mantisa += (1/2)**(i - 11)
    
    value = (-1 if (sign == '1') else 1) * (2**(exp - 1023)) * (1 + mantisa)

    print(format(value, ".5f"))
    print()
    
    # Question 2
    choppedVal = (int(value))
    print(choppedVal)
    print()

    # Question 3
    roundedVal = round(value)
    print(roundedVal)
    print()

    # Question 4
    absoluteError = abs(value - roundedVal)
    print(absoluteError)

    relativeError = absoluteError / value
    print(relativeError)
    print()

# Question 5 
def checkAleternating(function):
    if "-1**k" in function:
        return True
    return False

def checkDecreasing(function, x):
    decreasing = True
    k = 1
    startingVal = abs(eval(function))
    
    for k in range(2, 1000):
        result = abs(eval(function))
        if startingVal <= result:
            decreasing = False

    return decreasing

def minTerm(function, error):
    k = 1
    while abs(eval(function)) > error:
        k+=1
    print(k-1)
    print()

def bisection(function, accuracy, l, r):
    i = 0
    while abs(r - l) > accuracy and i <= 1000:
        i += 1

        m = (r + l) / 2
        x = m
        evalMid = eval(function)
        if(evalMid == 0):
            break

        x = l
        evalL = eval(function)
        condition1 = evalL < 0 and evalMid > 0
        condition2 = evalL > 0 and evalMid < 0
        if(condition1 or condition2):
            r = m
        else:
            l = m
            
    print(i)
    print()

def newtonRaphson(function, functionDir, x, accuracy):
    i = 0
    while(i < 1000):
        if eval(functionDir) != 0:
            i += 1
            xNext = x - eval(function) / eval(functionDir)
            if(abs(xNext - x) < accuracy):
                print(i)
                return
            x = xNext
    

if __name__ == "__main__":
    # Questions 1 - 4
    binary = "010000000111111010111001"
    doublePrecision(binary)

    # Question 5
    x = 1
    function = "(-1**k) * ((1**k) / (k**3))"

    checkAleternating = checkAleternating(function)
    checkDecreasing = checkDecreasing(function, x)

    if checkAleternating and checkDecreasing:
        minTerm(function, 1e-4)

    # Question 6
    left = -4
    right = 7
    function2 = "x**3 + 4 * (x**2) - 10"

    bisection(function2, 1e-4, left, right)

    functionDir = "3 * (x**2) + 8 * x"
    newtonRaphson(function2, functionDir, -4, 1e-4)