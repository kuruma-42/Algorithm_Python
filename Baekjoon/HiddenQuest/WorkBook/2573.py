
'''
baekjoon 2573 빙산

생각의 흐름
빙산이 있는 좌표 저장
Visited 만들고 탐색한다.
BFS해서 주변이 0이면 자신의 맵에서 숫자를 뺀다 수를 뺀다.

BFS가 한 바퀴 끝나면 DFS를 시작한다.
DFS에서 Connected Component가 2가 되는 순간
break하고 년도를 표시

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0

# 방향 벡터
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 빙산 덩어리 탐색 BFS
def bfs(sy, sx, visited, graph):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] > 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))

# 얼음 녹이기
# 이 쪽 로직이 핵심
# 구현 + 탐색
def melt(graph):
    new_graph = [row[:] for row in graph]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                water = 0
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0:
                        water += 1
                new_graph[i][j] = max(0, graph[i][j] - water)
    return new_graph

# 메인 시뮬레이션
while True:
    visited = [[False] * m for _ in range(n)]
    count = 0

    # Connected Component 수 세기
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited, graph)
                count += 1

    # 빙산이 두 개 이상으로 쪼개졌다면
    if count >= 2:
        print(year)
        break

    # 다 녹았다면
    if count == 0:
        print(0)
        break

    # 녹이고 연도 증가
    graph = melt(graph)
    year += 1
