'''
위상정렬 연습
21 04 15 15:55~ 
e, v, indegree, result
차수 0인거 꺼내서 인접 for문 돌면서 출력
- pop이 아니라 popleft
- indegree -- 는 큐에서 뺀 직후 for문 돌면서 뺴라.
'''

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
result = []

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    # 큐에서 뺐으니까 indegree 1빼야함.
    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)
            

for value in result:
    print(value, end=" ")

