def solution(strings, n):
    answer = []
    
    answer = strings
    answer.sort()
    answer.sort(key = lambda x:x[n])
    
    print(answer)
    
    return answer