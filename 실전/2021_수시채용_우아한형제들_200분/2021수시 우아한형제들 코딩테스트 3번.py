# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A_positive = [x for x in A if x > 0]
    A_positive.sort(reverse=True)
    A_negative = [x for x in A if x < 0]
    A_negative.sort()

    while(True) :
        if A_negative == [] or A_positive == []:
            break

        if abs(A_negative[0]) > A_positive[0]:
            del A_negative[0]
        elif abs(A_negative[0]) < A_positive[0]:
            del A_positive[0]
        elif abs(A_negative[0]) == A_positive[0]:
            return A_positive[0]

    return 0
 

A = [3,2,-2,5,-3]
print("\nResult: \n"+str(solution(A)))
print("""Expect:
3""")

A = [1,1,2,-1,2,-1]
print("\nResult: \n"+str(solution(A)))
print("""Expect:
1""")

A = [1,2,3,-4]
print("\nResult: \n"+str(solution(A)))
print("""Expect:
0""")