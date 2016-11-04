import numpy as np
from scipy import stats

def meanMedianMode():
    size = int(input())
    s = raw_input()
    numbers = list(map(int, s.split()))

    print(sum(numbers) / float(len(numbers)))

    print(np.median(numbers))
    print(int(stats.mode(numbers)[0]))


def weightedAvg():
    size = int(input())
    if size in range(5,51):
        total = 0.0
        s = raw_input()
        numbers = list(map(int, s.split()))

        w = raw_input()
        weights= list(map(int, w.split()))

        if all((item > 0 and item <=100) for item in numbers ) and all((item > 0 and item <=100) for item in weights ):

            for no, weight in zip(numbers, weights):
                total+=(no * weight)

            print round(total/sum(weights), 1)

weightedAvg()
