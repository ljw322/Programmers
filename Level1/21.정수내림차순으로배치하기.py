# 2021 03 02 16:10 ~ 16:13

def solution(n):
    answer = 0
    arr = []
    
    for _ in str(n):
        arr.append(int(_))
        
    arr.sort(reverse = True)
    
    temp = ''
    for _ in arr:
        temp += str(_)
        
    answer = int(temp)
        
    return answer