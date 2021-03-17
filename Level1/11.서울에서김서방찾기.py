def solution(seoul):
    answer = ''
    
    index = 0
    for _ in seoul:
        if _ == 'Kim':
            break
        index += 1
        
    answer = "김서방은 "+str(index)+"에 있다"
    
    return answer