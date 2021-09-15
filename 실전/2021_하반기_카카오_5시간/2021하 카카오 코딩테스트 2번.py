import math

def solution(n, k):
    answer = 0

    nthNumber = makeNthNumber(n, k)

    print(nthNumber)

    splited = str(nthNumber).split("0")

    print(splited)

    for item in splited:
        if item != '' and isPrime(int(item)) :
            answer += 1

    return answer

def makeNthNumber(n, k):
    num = 0
    answer = ""
    n = int(n)
    while n >= math.pow(k,num):
        num += 1
    
    while n > 0:
        num -= 1
        answer += str(int(n // math.pow(k,num)))
        n = n % math.pow(k,num)

    return answer

def isPrime(n):
    if n == 0 or n == 1:
        return False

    for i in range (2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


n = 437674
k = 3
print(solution(n, k))
print("expect = 3")

n = 110011
k = 10
print(solution(n, k))
print("expect = 2")

n = '01100110'
k = 10
print(solution(n, k))
print("expect = 2")
