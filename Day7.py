from math import sqrt

def standardaDeviation(numbers):
        mean = (sum(numbers) / float(len(numbers)))
        total = 0.0

        for item in numbers:
            current = (item - mean)
            total += (current * current)

        variance = total/len(numbers)
        return sqrt(variance)


def mean(x):
    return float(sum(x)/len(x))


def calPearson(x, y, m_x, m_y):
    total = 0.0
    for i, j in zip(x, y):
        sum_x = i-m_x
        sum_y = j-m_y
        total += sum_x*sum_y
        #print sum_x, sum_y, total
    #print total
    return total

def getRanks(x):
    newList = sorted(x)
    ranks ={}
    for no in x:
        ranks[no] = newList.index(no)+1
    return ranks

def spearmans():
    numScores = int(raw_input())
    if 10 <= numScores <= 100:
        X = (map(float, raw_input().split()))
        Y = (map(float, raw_input().split()))
        if all((1 <= item <= 500) for item in X) and all((1 <= item <= 500) for item in Y):
            r_x = getRanks(X)
            r_y = getRanks(Y)
            total = 0.0
            for x,y in zip(X,Y):
               total+= pow(r_x[x]-r_y[y], 2)
            print round(1.0 - ((6 * total)/(numScores*(pow(numScores, 2) -1))), 3)


def pearson1():
    numScores = int(raw_input())
    if 10<=numScores<=100:
        X = (map(float, raw_input().split()))
        Y = (map(float, raw_input().split()))
        if all((1<= item <= 500) for item in X) and all((1<= item <= 500) for item in Y):
            pearsonCoeff(X, Y, numScores)


def pearsonCoeff(X, Y, numScores):
    mean_x = mean(X)
    mean_y = mean(Y)
    sd_x = standardaDeviation(X)
    sd_y = standardaDeviation(Y)
    #print mean_x, mean_y, sd_x, sd_y
    return calPearson(X, Y, mean_x, mean_y) / (numScores * sd_x * sd_y)


def leastSquare():
    x = []
    y = []

    for i in range(5):
        input = raw_input()
        getInput(x, y, input)

    p = pearsonCoeff(x, y, 5)
    slope = (p * standardaDeviation(y))/standardaDeviation(x)
    a = mean(y) - (slope * mean(x))

    print round((slope*80) + a, 3)



def getInput(x, y, input):
    x.append(int(input.split()[0]))
    y.append(int(input.split()[1]))


leastSquare()