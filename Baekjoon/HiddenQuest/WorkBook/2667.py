# baekjoon 2667 단지 번호 붙이기
# 맵 형태의 그래프 문제
# 5 <= N <= 25 의 크기로 완전탐색이 가능한 문제이다.
# Connected Component의 갯수를 출력하고
# Connected Component안의 노드의 갯수를 각각 출력할 것

n = int(input())
arr = []
visited = [[0 for j in range(n)] for i in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
component_cnt = 0
node_cnt = 0
house_count: [int] = []

for _ in range(n):
    arr.append(list(map(int,input())))

def dfs(y: int, x: int):
    global node_cnt
    # 방문처리
    visited[y][x] = 1
    # 단지 내 집 갯수 추가
    node_cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # OverFlow Check(맵 밖으로 나갔는지 체크)
        if ny < 0 or nx >= n or nx < 0 or ny >= n:
            continue

        # 방문 체크
        if visited[ny][nx] == 1:
            continue

        # 단지가 없으면
        if arr[ny][nx] == 0:
            continue

        # 탐색 제개
        dfs(ny, nx)


for i in range(n):
    for j in range(n):
        # 방문하지 않고
        if visited[i][j] == 0 and arr[i][j] == 1:
            dfs(i, j)
            component_cnt += 1
            house_count.append(node_cnt)
            node_cnt = 0

print(component_cnt)
house_count.sort()

for i in range(len(house_count)):
    print(house_count[i])
