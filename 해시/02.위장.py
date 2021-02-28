# 2021 02 28 19:40 ~ 
# 1 2 1 -> 5, 

'''
https://ninano1109.tistory.com/8 참조함.
combination을 다 구할 필요가 없었음. 
모든 경우의 수들을 곱한 다음 아무것도 선택하지 않을 경우 -1 
'''
import itertools 

def solution(clothes):
    answer = 0
    closet = dict()
    for clothe in clothes:
        if clothe[1] in closet:
            closet[clothe[1]] += 1
        else:
            closet[clothe[1]] = 1
            
    clothes_num = []
    for key, value in closet.items():
        clothes_num.append(value)
        
    n = len(clothes_num)
    print(clothes_num)
    answer = 1
    for _ in clothes_num:
        answer *= (_+1)
    answer -= 1
    
    # answer = sum(clothes_num)
#     combiList = []
#     for i in range(1,n+1):
#         combiList.append(list(itertools.combinations(clothes_num,i)))

#     for i in range(len(combiList)):
#         for j in range(len(combiList[i])):
#             mul = 1
#             for k in range(len(combiList[i][j])):
#                 mul *= combiList[i][j][k]      
            # answer += mul
    
    
    return answer