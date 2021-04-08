def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    scoreA = 0
    scoreB = 0
    scoreC = 0
    
    n = len(answers)
    for i in range(n):
        if answers[i] == a[i%5]:
            scoreA += 1
        if answers[i] == b[i%8]:
            scoreB += 1
        if answers[i] == c[i%10]:
            scoreC += 1
    print(scoreA, scoreB, scoreC)
    
    topList = []
    topList.append([1,scoreA])
    topList.append([2,scoreB])
    topList.append([3,scoreC])
    topList.sort(key = lambda x:-x[1])
    print(topList)
    
    maxScore = topList[0][1]
    print("maxScore:", maxScore)
    for value in topList:
        Score = value[1]
        if Score == maxScore:
            answer.append(value[0])
        else:
            break
    print(answer)
    
    return answer