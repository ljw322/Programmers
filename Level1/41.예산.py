def solution(d, budget):
    answer = 0
    
    d.sort()
    print(d)
    sumBudget = 0
    for team in d:
        sumBudget += team
        answer += 1
        if sumBudget <= budget:
            continue
        else:
            answer -= 1
        
        
    return answer