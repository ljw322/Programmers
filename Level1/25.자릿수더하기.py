def solution(n):
    answer = 0

    for value in str(n):
        answer += int(value)
    
    return answer