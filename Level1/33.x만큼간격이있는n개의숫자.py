def solution(x, n):
    answer = []
    
    value = x
    for i in range(n):
        answer.append(value)
        value += x       
        
    return answer