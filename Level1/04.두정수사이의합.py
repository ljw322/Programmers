# 2021 03 1 00:50 ~ 51

def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        answer += i
    return answer