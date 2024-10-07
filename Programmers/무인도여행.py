'''
Programmers 무인도 여행 DFS
X는 갈 수 없는 곳
숫자는 갈 수 있는 곳
상하좌우로 움질일 수 있는 칸이 있음 -> dy, dx
지도의 칸에 있는 밸류 -> 머물 수 있는 일수

리턴 ->
각 커낵티드 컴퍼넌트들이 가지고 있는 밸류의 합을 구한 후
오름차순 정렬 후 리턴한다.

처음 dfs로 풀었을 때 재귀댑스 오류 때문에 통과가 안 됐다.
재귀 댑스를 늘려주니 런타임 에러가 풀렸다.

'''
import sys
sys.setrecursionlimit(100000)


a: [[str]] = []
n = 0
m = 0
visited: [[str]] = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
day = 0
ans_arr: [int] = []

def solution(maps):
    global day
    global n
    global m
    global visited
    answer = []
    # 맵의 길이
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for i in range(m)] for i in range(n)]
    # 지도 세팅
    for i in range(len(maps)):
        map = list(maps[i])
        a.append(map)

    for i in range(n):
        for j in range(m):
            # 바다가 아니고
            if a[i][j] != 'X' and visited[i][j] != 1:
                # 탐색
                dfs(i,j)
                # 최대 일수 어팬드
                ans_arr.append(day)
                # 날짜 초기화
                day = 0

    if len(ans_arr) == 0:
        return [-1]
    else:
        return sorted(ans_arr)

def dfs(sy, sx):
    global day
    global visited
    # 방문 처리
    visited[sy][sx] = 1
    # 날짜 더하기
    day += int(a[sy][sx])
    # 4방 탐색
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        # 오버플로우 체크
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        # 방문 체크
        if visited[ny][nx] != 0:
            continue
        # 바다라면 못 간다
        if a[ny][nx] == 'X':
            continue
        # 탐색
        dfs(ny, nx)



#
# from collections import deque
#
#
# def solution(maps):
#     dy = [-1, 0, 1, 0]
#     dx = [0, 1, 0, -1]
#     a: [[str]] = []
#     ans_arr: [int] = []
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[0 for i in range(m)] for i in range(n)]
#     # 지도 세팅
#     for i in range(len(maps)):
#         map = list(maps[i])
#         a.append(map)
#
#     for i in range(n):
#         for j in range(m):
#             # 바다가 아니고 방문 안 했으면 탐색
#             if a[i][j] != 'X' and visited[i][j] != 1:
#                 # 큐 생성
#                 q = deque()
#                 # 인큐
#                 q.append([i,j])
#                 # 방문 처리
#                 visited[i][j] = 1
#                 # 날짜 더하기
#                 day = int(a[i][j])
#
#                 while q:
#                     sy, sx = q.popleft()
#                     for i in range(4):
#                         ny = sy + dy[i]
#                         nx = sx + dx[i]
#
#                         if ny < 0 or ny >= n or nx < 0 or nx >= m:
#                             continue
#
#                         if visited[ny][nx] == 1:
#                             continue
#
#                         if a[ny][nx] == 'X':
#                             continue
#                         # 큐에 넣고
#                         q.append([ny,nx])
#                         # 방문 처리
#                         visited[ny][nx] = 1
#                         # 날짜 더하기
#                         day += int(a[ny][nx])
#                 # 총 날짜 어팬드
#                 ans_arr.append(day)
#
#     if len(ans_arr) == 0:
#         return [-1]
#     else:
#         return sorted(ans_arr)

