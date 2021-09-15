def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reportedList = []

    report = set(report)
    report = list(report)
    
    for id in id_list:
        reportedList.append([id, 0])

    for rep in report:
        splited = rep.split(' ')
        reporter = splited[0]
        reported = splited[1]

        for item in reportedList:
            if item[0] == reported:
                item[1] += 1
                break

    for rep in report:
        splited = rep.split(' ')
        reporter = splited[0]
        reported = splited[1]

        reporter_idx = id_list.index(reporter)
        reported_idx = -1
        for i in range(len(reportedList)):
            if reportedList[i][0] == reported:
                reported_idx = i
                break

        if reported_idx == -1: continue
    
        if reportedList[reported_idx][1] >= k:
            answer[reporter_idx] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]	
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
k = 2
print(solution(id_list, report, k))
print("expect = [2,1,1,0]")

id_list = ["con", "ryan"]	
report = ["ryan con", "ryan con", "ryan con", "ryan con"]	
k = 3
print(solution(id_list, report, k))
print("expect = [0,0]")
