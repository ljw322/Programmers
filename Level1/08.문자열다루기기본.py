def solution(s):
    answer = True
    n = len(s)
    if n == 4 or n == 6:
        for _ in s:
            if ord('0')<=ord(_)<=ord('9'): continue
            else: answer = False
    else:
        answer = False
    
    # print(ord('0'), ord('9'))
    
    
    return answer