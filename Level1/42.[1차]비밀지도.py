# 2021 03 03 15:50 ~ 15:

def setMap(map, arr, n):
    for a in arr:
        road = list(str(bin(a)[2:]))
        if len(road)<n:
            for i in range(n - len(road)):
                road.insert(0,'0') 
        map.append(road)

def PrintArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()
    print()

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    RealMap = [['0'] * n for i in range(n)]
        
    setMap(map1, arr1, n)
    setMap(map2, arr2, n)
    
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                RealMap[i][j] = '#'
            else:
                RealMap[i][j] = ' '   

    # PrintArr(map1)
    # PrintArr(map2)
    # PrintArr(RealMap)
    
    
    for i in range(n):
        sen = ''
        for j in range(n):
            sen += RealMap[i][j]
        print(sen)
        answer.append(sen)
    
    return answer