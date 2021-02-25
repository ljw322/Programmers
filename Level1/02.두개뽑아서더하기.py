# 2021 02 25 14:22 ~ 

# 집합배열에 넣기

def solution(numbers):
    answer = []
    n = len(numbers)
    arr = set()
    
    for i in range(n):
        for j in range(n):
            if j == i: continue
            else: arr.add(numbers[i]+numbers[j])
    
    answer = list(arr)
    answer.sort()
    
    return answer