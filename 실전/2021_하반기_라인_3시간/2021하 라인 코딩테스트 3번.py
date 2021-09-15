import copy

def solution(jobs):
    answer = []
    header = 0

    time = 0

    while jobs:
        if time < jobs[0][0]:
            time = jobs[0][0]
        
        list = []

        for i in range(0, len(jobs)):
            if time < jobs[i][0]: break
            if time >= jobs[i][0]:
                switch = False
                for j in list:
                    if jobs[i][2] == j[0]:
                        j[1] += jobs[i][3]
                        switch = True
                    
                if switch: continue
                list.append([jobs[i][2], jobs[i][3]])

            else:
                break
        list.sort()

        target = 0
        maxPriority = 0
        for item in list:
            if item[1] > maxPriority:
                target = item[0]
                maxPriority = item[1]

        if target != header:
            answer.append(target)
        header = target

        temp = copy.deepcopy(jobs)
        for i in range(len(jobs)):
            if jobs[i][0] > time:
                break
            if jobs[i][2] == target:
                time += jobs[i][1]
                temp.remove(jobs[i])

        jobs = copy.deepcopy(temp)

    return answer

jobs = [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]	
print(solution(jobs))
print("expect = [2, 1, 2, 3]")


jobs = [[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]]		
print(solution(jobs))
print("expect = [1, 2]")


jobs = [[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]
print(solution(jobs))
print("expect = [3, 4]")


jobs = [[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]		
print(solution(jobs))
print("expect = [1, 3, 4]")