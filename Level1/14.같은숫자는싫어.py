def solution(arr):
    answer = []
    
    answer.append(arr[0])
    for index in range(1, len(arr)):
        last = answer[-1]
        if arr[index] == last:
            continue
        else:
            answer.append(arr[index])            
    
    return answer