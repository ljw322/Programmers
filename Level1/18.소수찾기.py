#
'''
# 에라토스테네스의 체 이용!!
# 1은 제거.
# 지워지지 않은 수 중 제일 작은 수를 소수로 채택하고,
# 나머지 그 수의 배수를 모두 지운다.
https://wikidocs.net/21638
https://top100itw.medium.com/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%86%8C%EC%88%98%EC%B0%BE%EA%B8%B0-python-567a90d9f589
'''

# def isPrime(a):
#     if(a<2):
#         return False
#     for i in range(2,a):
#         if(a%i==0):
#             return False
#     return True

def solution(n):
    answer = 0
    
    numSet = set(range(2, n+1))
    for i in range(2, n+1):
        if i in numSet:
            numSet -= set(range(i*2, n+1, i))  
    
    answer = len(numSet)
    return answer