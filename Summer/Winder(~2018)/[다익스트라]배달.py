# 2021 04 14 13:20 ~ 14:00
# 다익스트라 알고리즘
# 양방향 노선. 프로그래머스. 전역변수 선언 input, distance
import heapq
import sys

INF = (1e9)
input = sys.stdin.readline

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
            
        

def solution(N, road, K):
    answer = 0
    global graph
    global distance
    graph = [[] for i in range(N+1)]
    distance = [INF]*(N+1)
    
    for value in road:
        a, b, c = value
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    start = 1 
    dijstra(start)

    print(distance)
    for i in range(1, N+1):
        if distance[i] != INF and distance[i] <= K:
            answer += 1
    return answer