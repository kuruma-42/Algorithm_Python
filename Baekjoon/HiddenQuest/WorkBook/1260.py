# baekjoon 1260 DFS와 BFS

#정점, 간선수, 시작점을 입력받음
n, m, v = map(int, input().split())
#초기값을 False로 만들어 그래프를 선언
graph =[[False] * (n+1) for _ in range(n+1)]

#연결된 정점을 입력
for i in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

print(graph)
# 1:[2,3,4] 2:[1,4] 3:[1,4] 4[1,2,3]