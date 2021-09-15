def solution(triangle):
    answer = 0

    if len(triangle) == 1:
        return triangle[0]
    else:
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

    for i in range(2, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    answer = max(triangle[len(triangle)-1])

    return answer
    

tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tri))
print("expect = 30")