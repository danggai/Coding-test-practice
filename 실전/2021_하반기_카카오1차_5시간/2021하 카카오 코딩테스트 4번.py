import copy

maxgap = 0
answer = [-1]

def solution(n, info):
    global answer

    dfs(n, info, [0,0,0,0,0,0,0,0,0,0,0], 10)

    return answer

def dfs(n, info, ryanInfo, index):
    global maxgap
    global answer
    if n < 0:
        return
    elif n == 0:
        gap = result(info, ryanInfo)
        if gap > maxgap:
            answer = ryanInfo
            maxgap = gap
        return
    elif index < 0 and n > 0:
        ryanInfo[10] += n
        gap = result(info, ryanInfo)
        if gap > maxgap:
            answer = ryanInfo
            maxgap = gap
        return


    newRyanInfo = copy.deepcopy(ryanInfo)
    newRyanInfo[index] += info[index] + 1

    dfs(n - info[index] - 1, info, newRyanInfo, index-1)
    dfs(n, info, ryanInfo, index-1)
    
def result(apeach, ryan):
    scoreApeach = 0
    scoreRyan = 0
    for i in range(0, 11):
        if (apeach[i] > ryan[i]):
            scoreApeach += 10 - i
        elif (apeach[i] < ryan[i]):
            scoreRyan += 10 - i
        
    return scoreRyan - scoreApeach


n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]	
print(solution(n, info))
print("expect = [0,2,2,0,1,0,0,0,0,0,0]")

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]		
print(solution(n, info))
print("expect = [-1]")

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]	
print(solution(n, info))
print("expect = [1,1,2,0,1,2,2,0,0,0,0]")

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))
print("expect = [1,1,1,1,1,1,1,1,0,0,2]")

n = 2
info = [0,1,0,0,0,0,0,0,0,0,1]
print(solution(n, info))