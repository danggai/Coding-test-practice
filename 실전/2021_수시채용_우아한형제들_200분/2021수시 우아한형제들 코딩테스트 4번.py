# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_origin(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1

def solution_modified(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        while (B[i] < a): i += 1
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1


A = [1,3,2,1]
B = [4,2,5,3,2]
print("\nOrigin: \n"+str(solution_origin(A, B)))
print("Modified: \n"+str(solution_modified(A, B)))
print("""Expect:
2""")

A = [2,1]
B = [3,3]
print("\nOrigin: \n"+str(solution_origin(A, B)))
print("Modified: \n"+str(solution_modified(A, B)))
print("""Expect:
-1""")

A = [100000]
B = [1,2,3,4,5,100000]
print("\nOrigin: \n"+str(solution_origin(A, B)))
print("Modified: \n"+str(solution_modified(A, B)))
print("""Expect:
100000""")


A = [1,2,3,4,5,100000]
B = [100000]
print("\nOrigin: \n"+str(solution_origin(A, B)))
print("Modified: \n"+str(solution_modified(A, B)))
print("""Expect:
100000""")


