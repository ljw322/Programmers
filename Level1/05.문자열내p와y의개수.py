def solution(s):
    answer = True
    
    s = s.lower()
    a = 0
    b = 0
    for _ in s:
        if _ == 'p': a += 1
        elif _ == 'y': b += 1
        else: continue
    
    if a != b: return False
    else: return True