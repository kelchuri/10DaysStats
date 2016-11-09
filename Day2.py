import numpy as np
import math

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def quartiles():
    size = int(input())
    if size in range(5, 51):
        q2 = 0.0
        s = raw_input()
        numbers = list(map(int, s.split()))
        if all((item > 0 and item <= 100) for item in numbers):
            q2 = median(numbers)
            numbers = sorted(numbers)
            if len(numbers) % 2 == 0:
                upperHalf = numbers[: (len(numbers) / 2)]
                lowerHalf = numbers[(len(numbers) / 2):]
            else:
                upperHalf = numbers[: len(numbers) / 2]
                lowerHalf = numbers[(len(numbers) / 2) + 1:]
            print int(median(upperHalf))
            print int(q2)
            print int(median(lowerHalf))

def calQuartiles(numbers):
    q2 = median(numbers)
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        upperHalf = numbers[: (len(numbers) / 2)]
        lowerHalf = numbers[(len(numbers) / 2):]
    else:
        upperHalf = numbers[: len(numbers) / 2]
        lowerHalf = numbers[(len(numbers) / 2) + 1:]

    return (median(upperHalf)), (median(lowerHalf))





def interQuartile():
    final = []
    size = int(input())
    if size in range(5, 51):
        s = raw_input()
        numbers = list(map(int, s.split()))
        f = raw_input()
        freq = list(map(int, f.split()))
        if all((item > 0 and item <= 100) for item in numbers) and all((item > 0 and item <= 1000) for item in freq):
            for no, fre in zip(numbers, freq):
                for i in range(fre):
                    final.append(no)

            if sum(freq) == len(final):
                q1,q3 = calQuartiles(final)
                print float(q3-q1)



def standardaDeviation():
    size = int(input())
    s = raw_input()
    if size in range(5, 101):
        numbers = list(map(int, s.split()))
        mean = (sum(numbers) / float(len(numbers)))
        total = 0.0
        if all((item > 0 and item <= 100000) for item in numbers):
            for item in numbers:
                current = (item - mean)
                total += (current * current)

            variance = total/size
            print round(math.sqrt(variance),1)

standardaDeviation()




