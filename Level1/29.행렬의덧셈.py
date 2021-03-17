# 2021 03 03 12:30 ~ 12:
def solution(arr1, arr2):
    answer = []
    
    n = len(arr1)
    m = len(arr1[0])
    
    print(n,m)
    
    for i in range(n):
        tempList = []
        for j in range(m):
            # print(arr1[i][j])
            
            tempList.append(arr1[i][j] + arr2[i][j])
        answer.append(tempList)
    
    return answer