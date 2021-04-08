# 2021 03-17 11:??~12:08

# 계수정렬 이용
# 도전한 사람이 0일 경우 예외 처리 해줘야 !

def solution(N, stages):
    answer = []
    failure = [0]*(N+2)
    countList = [0]*(N+2)
    order = []
    
    for value in stages:
        countList[value] += 1
        
    for i in range(1, N+1):
        b = 0
        for j in range(i, N+2):
            b += countList[j] 
        if b == 0:
            failure[i] = 0
        else:
            failure[i] = countList[i] / b
        # print("b:", b)
        
    # print(failure)   
    # print(countList)   
    for i in range(1, N+1):
        order.append([i, failure[i]])
    
    order.sort(key = lambda x : -x[1])
    
    for value in order:
        answer.append(value[0])
    
    return answer