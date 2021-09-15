def solution(jobs):
    time = 0
    spendtime = []
    answer = 0
    
    while jobs:
        if time < jobs[0][0]:
            time = jobs[0][0]
            
        idx = 0
        worktime = 1001
        for i in range(0, len(jobs)):
            if worktime > jobs[i][1] and time >= jobs[i][0]:
                worktime = jobs[i][1]
                idx = i
                
        time += jobs[idx][1]
        spendtime.append( time - jobs[idx][0])
        jobs.remove(jobs[idx])
        
    answer = sum(spendtime)//len(spendtime)
    
    return answer



jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))
    