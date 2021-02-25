
'''
2021 02 25 13:50 ~ 14:15
두 개의 스택을 이용하여 품

moves = [1,5,3,5,1,2,1,4]
0 0 0 0 0 
0 0 1 0 3
0 2 5 0 1 
4 2 4 4 2
3 5 1 3 1
'''

def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    
    for index in moves:
        # 젤 위에 있는 값을 stack에 담는다.(0이 아닌 값)
        for i in range(n):
            if board[i][index-1] == 0: continue
            else:
                # print('value:', board[i][index-1])
                stack.append(board[i][index-1])
                board[i][index-1] = 0
                break
    # stack = [4,3,1,1,3,2,4] -> 3113->4(터진 것의 갯수 출력)
    # print(stack)
    a = stack.pop()
    stack2 = []
    stack2.append(a)
    while stack:
        b = stack.pop()
        print("b, stack2[-1]", b, stack2[-1])
        
        if stack2[-1] == b:
            answer += 2
            stack2.pop()
        else: stack2.append(b)
    
    return answer