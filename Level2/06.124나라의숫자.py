# 210510 14:15 ~ 45,, 땡
# 210510 15:17 ~ 36.. 정답. 연습장에 생각해보고 풀으니 맞았다. 헝

def solution(n):
    answer = ''
    tempList = []
    rule = [4,1,2]

    while n > 0:
        m = n % 3
        n = n // 3
        
        if m % 3 == 0: n -= 1
        print("몫:", n)
        
        tempList.append(rule[m])
    
    print(tempList[::-1])
    for value in tempList[::-1]:
        answer += str(value)
    
    return answer