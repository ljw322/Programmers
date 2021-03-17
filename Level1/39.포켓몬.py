def solution(nums):
    answer = 0
    m = len(nums)//2
    
    kind = dict()
    for value in nums:
        if value in kind:
            kind[value] += 1
        else:
            kind[value] = 1
    print(kind)
    print(len(kind))
    if len(kind)>= m: answer = m
    else: answer = len(kind)
    
    
    return answer