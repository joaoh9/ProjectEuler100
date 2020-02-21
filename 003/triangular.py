import math


def getTerms(triangleNumber):

    tSqrt = round(math.sqrt(triangleNumber)) + 1

    terms = []

    for i in range(1, tSqrt):
        div = triangleNumber / i
        if triangleNumber % i == 0:
            terms.append(i)
            terms.append(round(div))
    terms.append(triangleNumber)
    return terms


def getTriangleNumber():
    i = 2
    termsSize = 0
    maxTerm = 0
    while termsSize < 500:
        triangleNumber = 0
        for j in range(1, i):
            triangleNumber += j
        terms = getTerms(triangleNumber)
        termsSize = len(terms)
        if maxTerm < termsSize:
            maxTerm = termsSize
        print(triangleNumber)
        # print(terms)
        print(termsSize)
        i += 1


def crivoErastothenes(n):
    crivo = [True] * n

    sqrtN = round(math.sqrt(n))

    for i in range(2, sqrtN + 1):
        if crivo[i] is True:
            k = 2
            x = k*i
            while x < n:
                crivo[x] = False
                k += 1
                x = k*i
    return crivo


def getPrimesFromCrivo(crivo):
    primes = []

    for i in range(0, len(crivo)):
        if crivo[i] is True:
            primes.append(i)

    return primes[1:]


def main():
    getTriangleNumber()


if __name__ == "__main__":
    main()
