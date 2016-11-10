from math import erf, sqrt


def fact(n):
    if n <= 1:
        return n
    else:
        return n * fact(n - 1)


def poisson1():
    avgLambda = float(raw_input())
    successK = int(raw_input())
    e = 2.71828

    print round((pow(avgLambda, successK) * pow(e, -avgLambda)) / fact(successK), 3)


def poisson2():
    input = raw_input()
    macA = float(input.split(" ")[0])
    macB = float(input.split(" ")[1])

    ca = 160 + 40 * (macA + pow(macA, 2))
    cb = 128 + 40 * (macB + pow(macB, 2))
    print round(ca, 3)
    print round(cb, 3)


def calERF(x):
    return erf(x)


def calNormal(x, avg, sd):
    e = 2.71828
    pi = 3.14
    num = pow(e, -(pow(x, 2) / 2))
    den = pow(2 * pi, 1 / 2)

    return 0.5 * (1 + calERF((x - avg) / (sd * sqrt(2))))


def normal1():
    input = raw_input()
    avg = int(input.split(" ")[0])
    deviation = int(input.split(" ")[1])
    variance = pow(deviation, 2)
    first = float(raw_input())
    input = raw_input()
    val1 = int(input.split(" ")[0])
    val2 = int(input.split(" ")[1])
    print calNormal(first, avg, deviation)
    print calNormal(val2, avg, deviation) - calNormal(val1, avg, deviation)


def normal2():
    input = raw_input()
    avg = int(input.split(" ")[0])
    deviation = int(input.split(" ")[1])
    variance = pow(deviation, 2)
    first = int(raw_input())
    second = int(raw_input())
    distSecond = calNormal(second, avg, deviation)
    print round(100 * (1.0 - calNormal(first, avg, deviation)), 2)
    print round(100 * (1.0 - distSecond), 2)
    print round(100 * (distSecond), 2)
    # print calNormal(val2, avg, deviation) - calNormal(val1,avg, deviation)

def central1():
    weight = int(raw_input())
    number = int(raw_input())
    avg = int(raw_input())
    sd = int(raw_input())

    new_avg = number * avg
    new_sd = sqrt(number) * sd

    print round(calNormal(weight, new_avg, new_sd), 4)

def central2():
    weight = int(raw_input())
    number = int(raw_input())
    avg = float(raw_input())
    sd = float(raw_input())

    new_avg = number * avg
    new_sd = sqrt(number) * sd

    print round(calNormal(weight, new_avg, new_sd), 4)

def central3():
    number = int(raw_input())
    avg = int(raw_input())
    sd = int(raw_input())
    cover = float(raw_input())
    z = float(raw_input())

    new_avg = number * avg
    new_sd = sqrt(number) * sd

    print round((new_avg - new_sd * z)/number, 2)
    print round((new_avg + new_sd * z) / number, 2)




central3()
