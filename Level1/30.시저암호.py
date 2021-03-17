def solution(s, n):
    answer = ''

    for value in s:
        if ord(value) == 32:
            answer += ' '
            
        if ord('a') <= ord(value) <= ord('z'):
            if ord(value)+n > ord('z'):
                answer += chr(ord(value)+n-26)
            else:
                answer += chr(ord(value)+n)
            
        if ord('A') <= ord(value) <= ord('Z'):
            if ord(value)+n > ord('Z'):
                answer += chr(ord(value)+n-26)
            else:
                answer += chr(ord(value)+n)
        
    
    return answer