# 2021 03 02 16:31 ~ 16:35

def solution(phone_number):
    answer = ''
    
    n = len(phone_number)
    
    answer += '*'*(n-4)
    if n>=4:
        answer += phone_number[-4:]
    print(answer)
    
    return answer