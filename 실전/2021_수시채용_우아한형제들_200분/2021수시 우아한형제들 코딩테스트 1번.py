# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(U, L, C):
    if U + L != sum(C):
        return "IMPOSSIBLE"

    first = ""
    second = ""

    for c in C:
        if c == 2:
            U -= 1
            L -= 1
            first += "1"
            second += "1"

        elif c == 1:
            if U > 0:
                U -= 1
                first += "1"
                second += "0"
            elif L > 0:
                L -= 1 
                first += "0"
                second += "1"

        elif c == 0:
            first += "0"
            second += "0"

    return first+","+second

 


U = 3
L = 2
C = [2,1,1,0,1]
print(solution(U,L,C))
print("expect = 11100, 10001")