# 2021 03 18 20:10 ~ 20:20
# https://m.blog.naver.com/PostView.nhn?blogId=jaeyoon_95&logNo=221732162754&proxyReferer=https:%2F%2Fwww.google.com%2F 블로그 보고 공부..
'''
n개의 음이 아닌 정수. 적절히 더하거나 빼서 타겟 넘버를 만듦
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

<input>
[1, 1, 1, 1, 1]	3	5

tree를 이용한 완전탐색
'''

def solution(numbers, target):
    tree = [0]
    
    for number in numbers:
        nodeList = []
        
        for node in tree:
            nodeList.append(node + number)
            nodeList.append(node - number)
        
        tree = nodeList
        
    answer = tree.count(target)
    return answer