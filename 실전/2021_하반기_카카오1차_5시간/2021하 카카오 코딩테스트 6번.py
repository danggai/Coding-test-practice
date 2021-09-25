import numpy as np

def solution(board, skill):
    answer = 0

    board_length = len(board)
    board_width = len(board[0])

    for item in skill:
        area = np.zeros((board_length, board_width))
        
        

    # for item in skill:
    #     for i in range(item[1], item[3]+1):
    #         for j in range(item[2], item[4]+1):
    #             if item[0] == 1:
    #                 board[i][j] -= item[5]
    #             if item[0] == 2:
    #                 board[i][j] += item[5]

    for item in board:
        for hp in item:
            if hp > 0:
                answer += 1

    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	
print(solution(board, skill))
print("expect = 10")

board = [[1,2,3],[4,5,6],[7,8,9]]	
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	
print(solution(board, skill))
print("expect = 6")

