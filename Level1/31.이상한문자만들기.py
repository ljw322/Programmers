def solution(s):
    answer = ''
    arr = s.split(" ")
    
    print(arr)
    for value in arr:
        for index in range(len(value)):
            if index % 2 == 0:
                answer += value[index].upper()
            else:
                answer += value[index].lower()
        answer += " "
        
    answer = answer[:-1]              
    
    return answer