# baekjoon 11404 플로이드
# n( 2 <= n <= 100 ) 도시
# m( 1 <= m <= 100,000 ) 개의 버스
# 모든 도시 쌍 (A , B)에 대해서 도시 A에서 B로 가는데 필요한 최솟값을 구하는 프로그램을 작성하시오
# 노드가 100개이다 플로이드 워셜을 고민해봐야한다.
# 모든 지점에서 모든 지점으로 가는 최소비용이면 플로이드 워셜을 써야한다.

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 1000_000_000

dist = [[INF for _ in range(n + 1)] for _ in range(n + 1) ]

# 대각선 1 만들기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dist[i][j] = 0

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    dist[u][v] = min(dist[u][v], w)

def floyd():
    # 간선을 노드 갯수 만큼 돌려준다.
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])


floyd()

for i in range(1, n + 1):
    line = []
    for j in range(1, n + 1):
        if dist[i][j] == [INF]:
            line.append[0]
        else:
            line.append(dist[i][j])

    print(' '.join(map(str, line)))