# baekjoon 7576 토마토 BFS
from collections import deque
m, n = map(int, input().split())
a = [list(map(int, input().split())) for j in range(n)]
arr: [int] = []
visited = [[0 for i in range(m)] for j in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0
flag = False

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and a[i][j] == 1:
            arr.append([i,j])

# 골드문제에서 난이도용으로 어렵게 낸 여러 곳에서 BFS를 시작하는 경우
def bfs(arr: [int]):
    global cnt
    q = deque()
    for i in range(len(arr)):
        q.append(arr[i])

    while len(q) != 0:

        t = q.popleft()
        # 토마토 익히고
        a[t[0]][t[1]] = 1

        for i in range(4):
            ny = t[0] + dy[i]
            nx = t[1] + dx[i]

            # 오버플로우 체크
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            # 방문 체크
            if visited[ny][nx] != 0: continue
            # 못가는 곳 체크
            if a[ny][nx] == -1: continue
            # 이미 토마토가 익었으면 안 가도 됨
            if a[ny][nx] == 1: continue
            # 큐에 넣고
            q.append((ny,nx))
            # 방문 처리
            visited[ny][nx] = visited[t[0]][t[1]] + 1

            cnt = max(cnt, visited[ny][nx])

bfs(arr)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            flag = True

if flag == True: print(-1)
elif cnt == 0: print(cnt)
else: print(cnt)

# 평범한 BFS
def bfs(y: int, x: int):
    global cnt
    q = deque()
    q.append((y,x))
    visited[y][x] = 1

    while len(q) != 0:

        t = q.popleft()
        # 방문 처리
        visited[t[0]][t[1]] = 1
        # 토마토 익히고
        a[t[0]][t[1]] = 1

        for i in range(4):
            ny = t[0] + dy[i]
            nx = t[1] + dx[i]

            # 오버플로우 체크
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            # 방문 체크
            if visited[ny][nx] != 0: continue
            # 못가는 곳 체크
            if a[ny][nx] == -1: continue
            # 큐에 넣고
            q.append((ny,nx))
            # 방문 처리
            visited[ny][nx] = visited[t[0]][t[1]] + 1

            cnt = max(cnt, visited[ny][nx])
