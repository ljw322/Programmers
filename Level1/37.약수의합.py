def solution(n):
    answer = 0
    arr = []
    
    for divider in range(1, n+1):
        if n % divider == 0: arr.append(divider)
            
    answer = sum(arr)
    return answer