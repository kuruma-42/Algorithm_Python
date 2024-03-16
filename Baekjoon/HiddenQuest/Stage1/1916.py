# baekjoon 1916 최소비용 구하기
# N개의 도시가 있다. 한 도시에 도착하는 버스가 M개 있다.
# A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# A번째 도시에서 B번째 도시까지 가는데 드는 최소 비용을 출력하라.
# 도시의 개수 1 <= N <= 1000 버스의 개수 1 <= M <= 100,100이 주어진다.
# 도시의 개수 N이 500이 넘어가기 때문에 플로이드는 쓰면 터질 확률이 있기 때문에
# 다익 스트라를 쓴다.

import sys
import heapq

# 도시의 개수
n = int(sys.stdin.readline())
# 버스의 개수 
m = int(sys.stdin.readline())
# 출발지, 도착지, 비용
a = [[] for _ in range(n + 1)]
# 최소 값 용 큰 값
INF = 1_000_000_000
# 테이블 정의
dist_table = [INF] * (n + 1)

for i in range(m):
    u, v, w =  map(int, sys.stdin.readline().split())
    a[u].append((v,w))

# 실제 출발지, 실제 도착지 
s, e = map(int, sys.stdin.readline().split(' '))

def dijkstra(start):
    # pq 생성 및 시작점의 거리를 초기화
    q = []
    # 시작점의 거리를 0으로 초기화
    heapq.heappush(q,(0, start))
    # Dist Table 갱신
    dist_table[start] = 0

    while q:
        # 시작점에서 u까지의 거리(d)가 가장 작은 것을 꺼내기
        # 최소힙이 기본이다.
        d, u = heapq.heappop(q)

        if dist_table[u] < d:
            continue

        # 현재 노드에서 방문 가능한 노드 갱신
        # dist_table[u] 확정된 최단거리
        for next in a[u]:
            # 이동 가능한 노드
            v, w = next
            # 경유 안 하고 이동하는 곳 > 경유해서 이동하는 것
            if dist_table[v] > dist_table[u] + w:
                dist_table[v] = dist_table[u] + w
                heapq.heappush(q, (dist_table[v], v))

dijkstra(s)

print(dist_table[e])