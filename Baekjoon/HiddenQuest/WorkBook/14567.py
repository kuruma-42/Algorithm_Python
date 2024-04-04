# baekjoon 14567 선수과목 (Topological Sort)
# 시간 제한 5초
# 어떤 과목들은 선수과목이 있어 해당하는 모든 과목을 먼저 이수해야만 과목을 이수할 수 있다.
# 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
# 모든 과목은 매 학기 항상 개설된다.
# 과뫅의 수 N 1<=N<=1000개
# 선수 조건의 수 M 1<=M<=500000개
# O(NM)만 되도 50억이 되서 터질 수 있다.

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
is_cycle = False
order = []

table = [0 for i in range(n + 1)]
adj_list = [[] for j in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    table[v] += 1


def topology_sort():
    q = deque()

    # 초기 세팅
    for i in range(1, n + 1):
        if table[i] == 0:
            q.append((i, 1))

    for i in range(1, n + 1):
        # 큐가 비어있는 경우
        if not q:
            global is_cycle
            is_cycle = True

        node = q.popleft()
        order.append(node)

        idx = node[0]
        term = node[1]

        for next in adj_list[idx]:
            # 진입 차선을 지워주고
            table[next] -= 1
            if table[next] == 0:
                q.append((next, term + 1))


topology_sort()
order.sort()
# print(is_cycle)
# print(order)
for node in order:
    idx = node[0]
    semester = node[1]
    print(semester, end=" ")


