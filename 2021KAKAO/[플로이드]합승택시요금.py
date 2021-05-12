# 2021 04 14 14:36 ~ 15:07
# 다익스트라, graph, distance
# 플로이드 워샬

# import heapq
# import sys
# input = sys.stdin.readline
INF = (1e9)

# def dijstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
    
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

def solution(n, s, a, b, fares):
    answer = INF
#     global graph
#     global distance
    
#     graph = [[] for i in range(n+1)]
#     distance = [INF] * (n+1)
    
#     for value in fares:
#         c, d, f = value
#         graph[c].append((d, f))
#         graph[d].append((c, f))
        
#     start = s
#     dijstra(start)
#     print(distance)
    graph = [[INF]*(n+1) for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
                
    for value in fares:
        c, d, f = value
        graph[c][d] = f
        graph[d][c] = f
        
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         print(graph[i][j], end=" ")
    #     print()
        
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    
    
    return answer