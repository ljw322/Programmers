# 2021 04 08 14:30 ~ 14:45
import math 

def yellowCase(yellowList, yellow):
    sqrt = int(math.sqrt(yellow))
    
    for i in range(1, sqrt+1):
        if yellow % i == 0:
            yellowList.append([i, yellow // i])

def solution(brown, yellow):
    answer = []
    yellowList = []
    
    yellowCase(yellowList, yellow)
    # print(yellowList)

    # 24 24 brown의 모서리를 제거하면 20
    # yellow가 기점 -> 만들 수 있는 사각형 만든다.(sqrt까지)
    '''
    1 24 -> 25*2
    2 12 -> 14*2
    3 8  -> 11*2
    4 6  -> 10*2 -> 
    '''
    for value in yellowList:
        a, b = value
        if (a+b)*2 == brown-4 :
            answer.append(b+2)
            answer.append(a+2)
            break    
    
    return answer