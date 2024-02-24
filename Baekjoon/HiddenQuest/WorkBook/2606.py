# baekjoon 2606 바이러스 (DFS, BFS)
# 네트워크를 통해 전파 네트워크 모델 = 그래프
# 컴퓨터의 수와 네크워크 상에서 서로 연결되어 있는 정보가 주어질 때
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

n = int(input())
e = int(input())
visited: [int] = [0 for i in range(n+1)]
ret = 0
# arr: [[int]] = [[]] * 8
arr = [[] for i in range(n+1)]

for i in range(e):
    n1,n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

def dfs(s: int):
    if visited[s] == 1: return
    global ret
    # 방문 처리
    visited[s] = 1
    ret += 1

    for i in arr[s]:
        # 방문했다면 continue
        dfs(i)


dfs(1)
print(ret - 1)