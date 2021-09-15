def solution(student, k):
    answer = 0

    for i in range(0, len(student)):
        for j in range(i+1, len(student)+1):
            _sum = sum(student[i:j])
            if (_sum) == k:
                answer += 1

    return answer

stu = [0,1,0,0]	
k = 1
print(solution(stu, k))
print("expect = 6")

stu = [0, 1, 0, 0, 1, 1, 0]	
k = 2
print(solution(stu, k))
print("expect = 8")

stu = [0, 1, 0]	
k = 2
print(solution(stu, k))
print("expect = 0")