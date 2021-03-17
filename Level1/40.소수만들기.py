from itertools import combinations

def isPrime(n): # 3 <= n
    count = 2
    for i in range(2, n):
        if n % i == 0: count += 1
    
    if count == 2: return True
    else: return False
    
    
def solution(nums):
    answer = 0
    
    result = list(combinations(nums,3))

    for value in result:
        sumResult = sum(value)
        if isPrime(sumResult): answer += 1
    
    return answer