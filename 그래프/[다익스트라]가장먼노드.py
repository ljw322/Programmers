# 2021 04 14 14:15 ~ 30
# 다익스트라. graph, distance - 최대인 것의 갯수
import heapq
import sys
input = sys.stdin.readline
INF = (1e9)

def dijstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            

def solution(n, edge):
    answer = 0
    global graph
    global distance
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    
    for value in edge:
        a, b = value
        graph[a].append((b, 1))
        graph[b].append((a, 1))
                        
    start = 1
    dijstra(start)
    
    # print(distance)
    
    maxValue = 0
    for i in distance:
        if i != INF and maxValue < i:
            maxValue = i
            
    print("maxValue:", maxValue)
    answer = distance.count(maxValue)
    
    return answer