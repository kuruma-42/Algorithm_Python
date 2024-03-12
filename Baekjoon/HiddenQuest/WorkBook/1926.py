# baekjoon 1926 그림
# 연결 컴포넌트 갯수, 가장 넓은 그림의 크기
# DFS로 풀면 런타임 에러가 난다 (Recursion Error)
# 함소호출 비용이 늘어나서임으로 재귀로 풀지 않고 BFS로 푼다.

'''
Recursion 오류의 예

def dfs(y: int,x: int):
    global cnt
    # 방문처리
    visited[y][x] = 1
    cnt += 1
    # 4방향 탐색
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 오버플로우 체크
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        # 그림이 없는 곳
        if a[ny][nx] == 0:
            continue

        if visited[ny][nx] != 0:
            continue

        # 방문
        dfs(ny, nx)

for i in range(len(paints)):
    # 그림이 있는 곳의 좌표
    y = paints[i][0]
    x = paints[i][1]
    # 그림이 있는 곳 중, 방문하지 않은 곳
    if a[y][x] == 1 and visited[y][x] == 0:
        # 방문
        dfs(y,x)
        # 커넥티드 컴퍼넌트 갯수 증가
        connected_component += 1
        ans = max(ans, cnt)
        cnt = 0
'''

import sys

n, m = map(int, sys.stdin.readline().split())
a = []
paints = []
visited = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
connected_component = 0
cnt = 0
ans = 0

for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    a.append(t)
    for j in range(m):
        paints.append([i, j])


def bfs(sy: int, sx: int):

    global cnt
    queue = []
    queue.append([sy, sx])
    visited[sy][sx] = 1

    while len(queue) != 0:
        cnt += 1
        q = queue.pop(0)

        for i in range(4):
            ny = q[0] + dy[i]
            nx = q[1] + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if visited[ny][nx] != 0:
                continue

            if a[ny][nx] == 0:
                continue

            queue.append([ny, nx])
            visited[ny][nx] = visited[q[0]][q[1]] + 1


for i in range(len(paints)):
    # 그림이 있는 곳의 좌표
    y = paints[i][0]
    x = paints[i][1]
    # 그림이 있는 곳 중, 방문하지 않은 곳
    if a[y][x] == 1 and visited[y][x] == 0:
        # 방문
        bfs(y,x)
        connected_component += 1
        ans = max(ans, cnt)
        cnt = 0


print(connected_component)
print(ans)






