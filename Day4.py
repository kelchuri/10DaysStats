import math
def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def combination(n,r):
    return fact(n)/(fact(n-r) * fact(r))

def power(num, pow):
    return math.pow(num, pow)

def calbinomial(n,r,p,q):
    return combination(n,r)*power(p, r)* pow(q, n-r)


def binomial1():
    input = raw_input()
    p = float(input.split(" ")[0])
    q = float(input.split(" ")[1])
    no = 6
    successCases = 3

    probabilityBoy = p/(p+q)
    probabilityGirl = 1-probabilityBoy
    print round(calbinomial(no, successCases, probabilityBoy, probabilityGirl)+calbinomial(no, successCases+1, probabilityBoy, probabilityGirl)+calbinomial(no, successCases+2, probabilityBoy, probabilityGirl)+calbinomial(no, successCases+3, probabilityBoy, probabilityGirl), 3)

def binomial2():
    input = raw_input()
    p = float(input.split(" ")[0])/100
    no = int(input.split(" ")[1])
    successCases = 2
    q= 1-p

    print round(calbinomial(no, successCases, p, q)+calbinomial(no, successCases-1, p, q)+calbinomial(no, successCases-2, p, q), 3)
    print round(1-(calbinomial(no,0,p,q) + calbinomial(no,1,p,q)),3)


def geometric1():
    input = raw_input()
    num = float(input.split(" ")[0])
    den = int(input.split(" ")[1])
    p= num/den
    q=1-p
    no = int(raw_input())
    print round(pow(q, no-1)*p, 3)

def geometric2():
    input = raw_input()
    num = float(input.split(" ")[0])
    den = int(input.split(" ")[1])
    p = num / den
    q = 1 - p
    no = int(raw_input())
    probabilityDefectNotFound = pow(q, no)
    print round(1-probabilityDefectNotFound, 3)

geometric2()