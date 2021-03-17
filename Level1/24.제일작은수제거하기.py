def solution(arr):
    answer = []
    
    min = 987654321
    for value in arr:
        if min >= value:
            min = value
    arr.remove(min)
    
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr
    
    return answer