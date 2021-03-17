# 20210317 13:30 ~ 14:30 
# S D T 
# 테스트케이스 6,7번을 해결하지 못함

def getScore(numList, count, score):
    temp = numList[count-1]
    if score == 'S': powValue = 1
    elif score == 'D': powValue = 2
    else: powValue = 3
        
    numList[count-1] = temp ** powValue

def updateScore(numList, count, option):
    
    if option == '*':
        numList[count-1] *= 2
        if count >= 2:
            numList[count-2] *= 2    
    else:
        numList[count-1] *= -1
    

    
def solution(dartResult):
    answer = 0
    
    count = 0
    n = len(dartResult)
    numList = []
    number = ''
    
    for i in range(0, n):
        # 숫자 뽑기
        if ord('0') <= ord(dartResult[i]) <= ord('9'):
            if dartResult[i+1] == '0':
                number = dartResult[i]
                continue
            else:
                if number:
                    a = number + dartResult[i]
                else:
                    a = dartResult[i]
                    
                count += 1
                numList.append(int(a))
                
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            getScore(numList, count, dartResult[i])
            # print(numList)
        
        if dartResult[i] == '*' or dartResult[i] == '#':
            updateScore(numList, count, dartResult[i])
            # print(numList)
        
            
    print(numList)
    answer = sum(numList)
    
    return answer