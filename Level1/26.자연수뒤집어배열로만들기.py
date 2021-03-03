# 2021 03 02 16:26 ~ 16:26

def solution(n):
    answer = []
    
    n = str(n)[::-1]
    for value in str(n):
        answer.append(int(value))       
    
    
    return answer