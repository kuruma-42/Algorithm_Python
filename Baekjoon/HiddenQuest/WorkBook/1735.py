# baekjoon 1735 최단경로
# 방향그래프가 주어지면
# '주어진 시작점에서 다른 모든 정점으로 최단경로를 구하는'
# 간선의 가중치는 10이하의 자연수
# 간선의 가중치와
# 정점의 갯수 V 간선의 갯수 E
# 모든 정점에는 1부터 V까지 번호가 매겨져 있음
# 둘째 줄에는 시작 정점의 번호 K가 주어진다.
# u -> v 로가는 가중치 w 간선이 존재.
# 정점 사이에 여러 개의 간선이 존재할 수 있다.
# 경로 존재하지 않는 경우 INF
# 수가 커서 pypy3로 해야 풀림
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

adjList = [[] for i in range(n + 1)]

# 간선 갯수 만큼 반복문
for i in range(m):
    u, v, w = map(int, input().split())
    # 도착지와 가중치를 튜플로 묶어서 인접리스트에 저장
    adjList[u].append((v, w))

INF = 1_000_000_000
# 방문과 거리를 잰다.
dist_table = [INF] * (n + 1)
ans = ""


def dijkstra(start):
    # 빈 큐 생성
    q = []
    # 힙큐에 푸쉬 (가중치, 출발지)
    heapq.heappush(q, (0, start))
    # 출발하는 곳 거리 0
    dist_table[start] = 0

    # q에 값이 없을 때 까지
    while q:
        # 시작 점에서 u까지 거리가 가장 작은 것을 꺼낸다.
        d, u = heapq.heappop(q)
        # u -> v로 가는 간선이 여러 개 존재 가능하기 때문에
        # dist_table[u]가 d 보다 작다는 것은 이미 최단거리가 확정됐다는 것이다.
        if dist_table[u] < d:
            continue

        # 현재 노드에서 방문 가능한 곳
        for next in adjList[u]:
            v, w = next
            # 도착할 곳의 거리가 현재 노드 + 가중치 보다 크다면 (INF)
            if dist_table[v] > dist_table[u] + w:
                dist_table[v] = dist_table[u] + w
                heapq.heappush(q, (dist_table[v], v))


dijkstra(start)

for i in range(1, n + 1):
    if dist_table[i] == INF:
        ans += "INF\n"
    else:
        ans += str(dist_table[i]) + "\n"

print(ans)
