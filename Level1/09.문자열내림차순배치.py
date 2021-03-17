def solution(s):
    answer = ''
    temp = []
    for _ in s:
        temp.append(_)
    
    temp.sort(reverse = True)

    for _ in temp:
        answer += _
    return answer