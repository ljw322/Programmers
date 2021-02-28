# 2021 02 28 18:40 ~ 53
'''
앞번호가 같은(접두사) 찾기
'''

def solution(phone_book):
    answer = True
    n = len(phone_book)
    
    flag = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            
            if len(phone_book[i]) <= len(phone_book[j]):
                m = len(phone_book[i])
                print(phone_book[i][:m], phone_book[j][:m])
                if phone_book[i][:m] == phone_book[j][:m]:
                    answer = False
                    flag = 1
                    break
        if flag == 1: break    
    
    return answer