# baekjoon 11000 강의실 배정 (그리디)
# Si에 시작해서 Ti에 끝나는 N개의 수업이 주어진다.
# '최소'의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
# 1<=N<=200,000
# 0 <= S < T <= 10^9
# 기준 시작 시간이 작고 끝나는 시간도 작고
# 수업 종료가 다음 수업 시작 보다 크면 heappush
# 수업 종료가 다음 수업 시작 보다 작으면 heappop 그리고 heappush
# 입력 값이 크기 때문에 input으로 받으면 안 되고, sys.stdin.readlin()로 받아야 한다.

# from queue import PriorityQueue
import sys
import heapq

n = int(input())
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
room = []

# for i in range(n):
#     start, end = map(int, input().split())
#     q.append([start, end])

q.sort()

# 강의실에 끝나는 시간을 넣어준다.
heapq.heappush(room, q[0][1])

for i in range(1, n):
    # 현재 회의실 끝나는 시간보다 다음 강의 시작시간이 빠르면
    if q[i][0] < room[0]:
        # 새로운 회의실 개설
        heapq.heappush(room, q[i][1])
    # 현재 회의실 끝나는 시간보다 다음 강의 시작 시간이 느리면
    else:
        # 강의실 빼주고
        heapq.heappop(room)
        # 다시 채워준다.
        heapq.heappush(room, q[i][1])

print(len(room))


