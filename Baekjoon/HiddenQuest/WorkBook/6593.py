'''
baekjoon 6593 상범 빌딩
상범 빌딩은 각 변의 길이가 1인 정육면체로 이루어져있다.
인접한 6개의 칸 동서남북'상''하'를 통해서 이동할 수 있다.
'대각선 이동은 불가능하다.
바깥면도 이동할 수 없다.
탈출할 수 있다면
' Escaped in x minute(s). ' 출력

탈출이 불가능 하다면
' Trapped! ' 출력

입력 받는 게 어렵다 ..

사고과정
1. 층을 탐색하는 로직을 짜야 함.
2. 상하좌우 + 위 아래
- dx, dy, dz를 만든다.
3. 최단거리 로직이기 때문에 BFS에 Visited에 1씩 더해주면 된다.

배운점
- 출력 문자 복사하기.
- 가상차원 (벽 부시고 이동하기)

'''
from collections import deque
import sys
input = sys.stdin.readline

dz = [0, 0, 0, 0, 1, -1]  # 위아래
dy = [-1, 0, 1, 0, 0, 0]  # 사방 탐색
dx = [0, 1, 0, -1, 0, 0]

while True:
    l, r, c = map(int, input().rstrip().split())
    if l == 0 and r == 0 and c == 0:
        break

    a: [[[str]]] = [[[] * c for j in range(r)]for i in range(l)]
    visited = [[[0 for k in range(c)] for j in range(r)] for i in range(l)]
    q = deque()

    for i in range(l):
        a[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()

    def go(sz: int, sy: int, sx: int):
        q.append([sz, sy, sx])
        visited[sz][sy][sx] = 1
        while q:
            z, y, x = q.popleft()
            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c:
                    if a[nz][ny][nx] == 'E':
                        print("Escaped in {0} minute(s).".format(visited[z][y][x]))
                        return

                    if a[nz][ny][nx] == '.' and visited[nz][ny][nx] == 0:
                        visited[nz][ny][nx] = visited[z][y][x] + 1
                        q.append([nz, ny, nx])

        print("Trapped!")

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if a[i][j][k] == 'S':
                    go(i, j, k)