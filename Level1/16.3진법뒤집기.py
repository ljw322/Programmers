def solution(n):
    answer = 0
    
    threeEx = ''
    while n > 0:
        if n % 3 == 0: threeEx += '0'
        else: threeEx += str(n % 3)
        n = n//3
    
    count = 1
    for value in reversed(threeEx):
        answer += int(value) * count
        print(answer)
        count*=3
        
    return answer