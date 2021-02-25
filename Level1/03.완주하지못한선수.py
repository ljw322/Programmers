'''
2021 02 05 14:33 ~ 42 50점/효율성 0점

해시문제. 리스트 반복문으로 풀면 안됨. 딕셔너리 이용해서 품
'''

def solution(participant, completion):
    answer = ''
    participants = dict()
    for name in participant:
        if name in participants:
            participants[name] += 1
        else:
            participants[name] = 1
    
    for name in completion:
        if name in participants:
            participants[name] -= 1
            
    # print(participants)
    
    # value값이 1이상인 값의 key 출력
    for key, value in participants.items():
        if value == 1:
            print(key)
            answer = key
    
    return answer