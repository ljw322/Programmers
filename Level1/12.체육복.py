# 2021 03 1 01:31 ~ 
'''
5번 : 5 [2, 3, 4] [1, 2, 3] 4
[1, 1, 1, 0, 1]
12번 : 5 [1, 2, 3] [2, 3, 4] 4
'''
def solution(n, lost, reserve):
    answer = 0
    board = [1]*n
    
    for _ in lost:
        board[_-1] = 0
    # print("before:",board)
    
    index = 0
    # 먼저 자기 자신 것이 도난 당한 것이 있는지부터 확인
    for _ in lost:
        if _ in reserve:
            board[_-1] = 1
            reserve.remove(_)
    print(board)
    
    for _ in board:
        if _ == 0: # 도난당한 사람
            # if index+1 in reserve:
            #     board[index] = 1
            #     reserve.remove(index+1)
            if index+1-1 in reserve:
                board[index] = 1
                reserve.remove(index+1-1)
            elif index+1+1 in reserve:
                board[index] = 1
                reserve.remove(index+1+1)
        
        index += 1
        
    print("after:", board, reserve)
    for _ in board:
        if _ == 1: answer += 1
    
    return answer