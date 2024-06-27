'''
Baekjoon 11724 연결요소의 개수
무방향 그래프의 연결요소 개수 구하는 프로그램 작성
정점의 개수 N 간선의 개수 M이 주어짐

1 <= N <= 1000
0 <= M <= N(N-1)/2 (M 범위가 좀 특이함)

예를 들면, 노드가 4개면
ex) 0 <= M <= 6

'''
'''
Baekjoon 11724 연결요소의 개수
무방향 그래프의 연결요소 개수 구하는 프로그램 작성
정점의 개수 N 간선의 개수 M이 주어짐

1 <= N <= 1000
0 <= M <= N(N-1)/2 (M 범위가 좀 특이함)

예를 들면, 노드가 4개면
ex) 0 <= M <= 6

'''

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split(' '))
visited = [0] * (n + 1)
ans = 0

arr: [[int]] = [[] for _ in range(n+1)]

def go(node):
    # 연결리스트 순회
    for next_node in arr[node]:
        # 방문 체크
        if visited[next_node] == 1:
            continue
        visited[next_node] = 1
        go(next_node)


for i in range(m):
    u, v = map(int, input().split(' '))
    arr[u].append(v)
    arr[v].append(u)

for node in range(1, n + 1):
    if visited[node] == 0:
        # 방문처리
        visited[node] = 1
        go(node)
        ans += 1

print(ans)
