# baekjoon 10026 적록색약
# 커낵티드 컴퍼넌트 응용 탐색
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

a =  [list(str(input()).rstrip()) for i in range(n)]
visited = [[0 for i in range(n)] for j in range(n)]
visited1 = [[0 for i in range(n)] for j in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
color = ['R','G','B']
color1 = ['R', 'B']
cnt = 0
cnt1 = 0
start_color = ""

def dfs(y: int, x: int):
    # 방문 처리
    visited[y][x] = 1

    for i in range(0,4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue

        if visited[ny][nx] == 1:
            continue

        if start_color != a[ny][nx]:
            continue

        dfs(ny, nx)

def dfs_color(y: int, x: int):
    # 방문 처리
    visited1[y][x] = 1

    for i in range(0,4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue

        if visited1[ny][nx] == 1:
            continue

        # 컬러가 달라
        if start_color != a[ny][nx] :
            # 시작 색이 블루나 도착 색이 블루면 컨틴뉴
            if start_color == 'B' or a[ny][nx] == 'B':
                continue

        dfs_color(ny, nx)

for i in color:
    start_color = i

    for j in range(n):
        for k in range(n):
            # 방문하지 않았고 스타트 컬러와 같을 것
            if visited[j][k] == 0 and a[j][k] == start_color:
                dfs(j,k)
                cnt += 1

            if visited1[j][k] == 0 and a[j][k] == start_color:
                dfs_color(j, k)
                cnt1 += 1

print("{0} {1}".format(cnt, cnt1))



