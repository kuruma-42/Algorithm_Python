# baekjoon 9466 텀 프로젝트
# 시간 제한이 3초, 정답 비율 23% 심상치 않은 문제다.
# 팀원 수에는 제한이 없다.
# 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 하고싶은 학생을 선택해야 한다
# ('단 한 명만 선택할 수 있다) (혼자 하고 싶어하는 학생은 자기 자신을 선택 가능)
# 학생들이 한 명씩 바로 옆의 학생을 선택하고 마지막 학생이 첫 번째 학생을 선택하면 된다.
# 학생들의 수는 (2<= n <= 100,000)이고 3초가 주어져있다. 그래도 O(n^2)까지 가면 위험할 것 같다.
import sys
from collections import deque

# 테스트 케이스 갯수
t = int(sys.stdin.readline())

for i in range(t):
    # 학생 수 (노드의 갯수로 생각하면 될까?)
    n = int(sys.stdin.readline())
    # 학생들이 선택한 파트너
    arr = list(map(int, sys.stdin.readline().split()))
    # 선택된 파트너를 체크하는 배열
    visited = [0] * (n + 1)
    real_visited = [0] * (n + 1)
    node = [[] for _ in range(n + 1)]


    def bfs(start:int):
        q = deque()
        q.append(node[start][0])
        visited_queue = []
        is_cycle = False
        last = 0
        while q:
            t = q.popleft()
            last = t
            # 이미 선택 받은 친구라면 건너 뛴다.
            if start == node[t][0]:
                is_cycle = True

            visited_queue.append(t)

            if visited[t] != 0:
                continue

            # 큐에 넣는다.
            q.append(node[t][0])

            # 방문 처리
            visited[t] = 1

        if is_cycle:
            for i in visited_queue:
                real_visited[i] = 1

    # print(arr)

    for i in range(n):
        node[i+1].append(arr[i])

    for i in range(1,n + 1):
        if real_visited[i] == 0:
            bfs(i)

    cnt = 0
    for i in real_visited:
        if i == 0:
            cnt += 1

    print(cnt - 1)



