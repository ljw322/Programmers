# 2021 04 08 13:40 ~ 14:30
# 소수판별에서 시간초과.!!! sqrt를 이용하여 시간을 줄일 것!!

from itertools import permutations
import math

# 소수판별 함수
def isPrime(num):
    count = 0
    sqrt = int(math.sqrt(num))
    if num != 0 and num != 1:
        for i in range(2, sqrt+1):
            if num % i == 0: count += 1
        
        if count == 0 : return True
        else: return False
    else: return False

# 숫자 조합

def solution(numbers):
    answer = 0
    # numList = list(numbers)
    numList = []
    numSet = set()
    
    
    for value in numbers:
        numList.append(value)
    # print(numList)
    
    for i in range(1, len(numList)+1):
        temp = list(permutations(numList,i))
        
        for a in temp:
            madeNumber = ''
            for b in a:
                madeNumber += b
                # print(madeNumber)
                numSet.add(int(madeNumber))
    print("numSet:", numSet)
    
    for value in list(numSet):
        if isPrime(value) == True:
            answer +=1     
            
    print(isPrime(1))
    
    return answer