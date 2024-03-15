# Dijkstra(다익스트라 - 최단 경로)
"""
    최소비용 구하기(dijkstra)

"""
import sys
import heapq

input = sys.stdin.readline

# 도시의 개수(정점)
n = int(input())
# 버스의 개수(간선)
m = int(input())

adjList = [[] for i in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adjList[u].append((v, w))

s, e = map(int, input().split())

INF = 1_000_000_000
dist_table = [INF] * (n + 1)

# dist_S [1,2,3,4,5,6]
# 중간 합승지역이 1이라면

# dist_A [1,2,3,4,5,6]
# dist_B [1,2,3,4,5,6]
# 특별한 경우 아니면 heapq를 사용하여 구현한다.
# heapq.heappush(list, (정렬기준, 값))
# default minHeap 제공
def dijkstra(start):
    # pq 생성 및 시작점의 거리를 초기화
    q = []
    heapq.heappush(q, (0, start))
    dist_table[start] = 0

    while q:
        # 시작점에서 u까지 거리(d)가 가장 작은것 을 꺼내기.
        d, u = heapq.heappop(q)

        # 방문하면, 최단거리가 확정이된다 --> 이미 방문되어 최단거리가 정해진 노드(visited)
        if dist_table[u] < d:
            continue

        # 현재 노드에서 방문 가능한 노드 갱신
        # dist_table[u] 확정된 최단거리.
        for next in adjList[u]:
            v, w = next
            if dist_table[v] > dist_table[u] + w:
                dist_table[v] = dist_table[u] + w
                heapq.heappush(q, (dist_table[v], v))


if __name__ == '__main__':
    dijkstra(s)
    print(dist_table[e])
