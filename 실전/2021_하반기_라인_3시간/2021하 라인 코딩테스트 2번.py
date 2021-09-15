def alphaToNum(char) :
    return ord(char) - 97

def numToAlpha(num) :
    return chr(num + 97)

def solution(research, n, k):
    answer = "None"

    list = [[0 for i in range(len(research))] for _ in range(0,26)]

    for a in range(len(research)):
        for _char in research[a]:
            list[alphaToNum(_char)][a] += 1

    best = [0 for _ in range(0,26)]

    for a in range(0,26):
        for b in range (0,len(research)-n+1):
            switch = False
            sum = 0
            for c in range (b,b+n):
                sum += list[a][c]
                if list[a][c] < k:
                    switch = True
            if switch: break
            if sum >= 2 * n * k:
                best[a] += 1

    print(best)

    max = 0
    for i in range(len(best)):
        if best[i] > max:
            answer = numToAlpha(i)
            max = best[i]

    return answer

res = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]	
n = 2
c = 2
print(solution(res, n, c))
print("expect = a")

res = ["yxxy","xxyyy"]	
n = 2
c = 1
print(solution(res, n, c))
print("expect = x")

res = ["yxxy","xxyyy","yz"]	
n = 2
c = 1
print(solution(res, n, c))
print("expect = y")

res = ["xy","xy"]
n = 1
c = 1
print(solution(res, n, c))
print("expect = None")