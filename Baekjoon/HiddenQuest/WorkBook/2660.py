# baekjoon 2660 회장뽑기 BFS
# 회원수 50이하 (완전탐색이 가능하다)
# 몇 사람을 통하면 모두가 서로 알 수 있다 (연결되어있지 않은 노드가 없다)
# bfs로 visited에 표시
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
candidate = []

while True:
    f1, f2 = map(int, sys.stdin.readline().split())
    if f1 == -1 and f2 == -1:
        break

    arr[f1].append(f2)
    arr[f2].append(f1)

def bfs(start: int):
    q = deque()
    for node in arr[start]:
        q.append(node)
        visited[node] = 1

    while q:
        t = q.popleft()
        if t == start:
            continue

        for next in arr[t]:

            if visited[next] != 0:
                continue

            q.append(next)
            visited[next] = visited[t] + 1

for i in range(1,n+1):
    bfs(i)
    # 양방향 간선이기 때문에, 탐색을 시작한 노드로 다시 돌아가는 것은 visited가 0 이 아니라
    # 2가 될 확률이 있기 때문에 자기 자신의 방문 값은 0으로 초기화 해줘야한다.
    visited[i] = 0
    t = max(visited)
    candidate.append(t)
    visited = [0] * (n + 1)

print(min(candidate), candidate.count(min(candidate)))
for i in range(len(candidate)):
    if candidate[i] == min(candidate):
        print(i+1, end=' ')


