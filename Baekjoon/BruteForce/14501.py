'''
baekjoon 14501 퇴사
인덱스 + 걸리는 날짜를 더한 이후의 값n 개를 전부 계산한다
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

3 10 선택
22 15 선택 등등
index + 소요일이 n보다 크면 멈춘다.

N은 1000개 까지이다 n^2 까지 허용
재귀로 풀어야 함.
DFS 탐색인 것을 알아야 한다.
'''

import sys
n = int(sys.stdin.readline())
days, pays = [], []

for _ in range(n):
    t, p = map(int, sys.stdin.readline().split(' '))
    days.append(t)
    pays.append(p)

max_profit = 0

def dfs(day, profit):
    global  max_profit
    # 날짜가 n보다 크면
    if day >= n:
        max_profit = max(max_profit, profit)
        return

    # 현재 날짜 + 상담 소요 날짜가 n 보다 작으면
    if day + days[day] <= n:
        # 날짜에 오늘 + 상담 소요 날짜 증가
        # 지금 까지의 이윤 + 오늘 이윤
        dfs(day + days[day], profit + pays[day])
    # 상담을 안 하면 그냥 넣어 준다.
    dfs(day + 1, profit)

dfs(0, 0)
print(max_profit)