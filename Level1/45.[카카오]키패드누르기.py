#2021 03 18 19:00 ~ 20:00 
# 좌표 계산으로 가자

def calDistance(keypad, lr, value):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    for _ in keypad:
        if lr in _[0] :
            x1, y1 = _[1]
            
    for _ in keypad:
        if value in _[0] :
            x2, y2 = _[1]
            
    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):
    answer = ''
    
    keypad = []
    
    num = 1
    for i in range(3):
        for j in range(3):
            keypad.append([str(num), [i, j]])
            num += 1
    keypad.append(['*',[3,0]])
    keypad.append(['0',[3,1]])
    keypad.append(['#',[3,2]])

    print(keypad)    
    
    lstack = ['*']
    rstack = ['#']
    L_index = ['1', '4', '7', '*']
    R_index = ['3', '6', '9', '#']
    M_index = ['2', '5', '8', '0']
    
    for value in numbers:
        value = str(value)
        
        if value in L_index:
            lstack.append(value)
            answer += 'L'
        
        elif value in R_index:
            rstack.append(value)
            answer += 'R'
            
        else:
            left = lstack[-1]
            right = rstack[-1]
            
            if calDistance(keypad, left, value) > calDistance(keypad, right, value):
                rstack.append(value)
                answer += 'R'
            elif calDistance(keypad, left, value) < calDistance(keypad, right, value):
                lstack.append(value)
                answer += 'L'
            else:
                if hand == "left":
                    lstack.append(value)
                    answer += 'L'
                else:
                    rstack.append(value)
                    answer += 'R'  
    
    
    return answer