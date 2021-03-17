def solution(x):
    answer = True
    
    sumValue = 0
    for value in str(x):
        sumValue += int(value)
        
    if x % sumValue != 0: answer = False
        
    return answer