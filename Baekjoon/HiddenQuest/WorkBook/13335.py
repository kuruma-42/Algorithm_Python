
'''
baekjoon 13335 트럭

다리를 n개의 트럭이 지나가려고 한다. 트럭의 순서는 바꿀 수 없다.
트럭의 수 n
다리 길이 w
최대 하중 L

다리를 실제 건넌다고 생각 안 하고
트럭이 있는 배열에서 생각하면 어떨까? x
포인터를 n개 쓴다? x
슬라이딩 윈도우로 푼다? X

다리 길이 = 윈도우의 길이
최대 하중 = 윈도의 요소들의 크기의 합
[           ] 배열 크기를 정해서 크기를 맞추자
처음을 0으로 채워넣는다.
못 들어가는 시간을 0으로 넣는다

q를 따로 만든다.
그 q에 들어간 길이 만큼 답이 된다.


l = 4
w = 2
[       2, 0  ]         3
[2, 2, 0 , 0 ,0 , ]
'''

import sys

n, w, l = map(int, sys.stdin.readline().split(' '))
q = list(map(int, sys.stdin.readline().split(' ')))
# 일단 0으로 설정해준다.
b = [0] * w
# 이게 답
cnt = 0
# 마지막 트럭이 들어오고 그 트럭이 빠져나갈 때 까지 (queue가 다 지나갈 때 까지
while b:
    # while문이 한 번 돌면 우선 1초라 생각하고 +1 한다
    cnt += 1
    # 제일 첫 번째 값 pop
    b.pop(0)
    # 트럭이 존재한다면
    if q:
        # 다리위의 무게 + 새로운 트럭의 무게가 최대 하중 보다 작거나 같다면
        if sum(b) + q[0] <= l:
            # 트럭을 다리위에 올린다
            b.append(q.pop(0))
        else:
            # 아니면 0을 더해준다.
            b.append(0)
print(cnt)




'''
잘못된 풀이 
기준을 잘 잡아야 함 
기준을 시간으로 잡아야 함 
트럭을 기준으로 잡고 돌리면 안 되는 문제 
'''
# import sys
# from collections import deque
#
# n, w, l = map(int, sys.stdin.readline().split(' '))
# a = list(map(int, sys.stdin.readline().split(' ')))
# window = deque()
# window_value = 0
# cnt = 0
# ans = [0] * w
#
# for truck in a:
#     # 다음 트럭 진입하려고 함
#     if len(window) < w:
#         # 만약 다리 위의 차의 무게와 새로 진입하는 차의 무게가 크다면
#         if (window_value + truck) > l:
#             # 다리 위의 차 + 새로 진입하는 차의 무게가 l과 같거나 작아질 때 까지 팝한다.
#             while (window_value + truck) > l:
#                 minus_val = window.popleft()
#                 window_value -= minus_val
#                 window.append(0)
#                 ans.append(0)
#                 cnt += 1
#             window_value += truck
#             window.append(truck)
#             ans.append(truck)
#         else:
#             window_value += truck
#             window.append(truck)
#             ans.append(truck)
#     else:
#         # 숫자가 꽉 찾으면 pop 한다
#         minus_val = window.popleft()
#         # pop한 숫자를 다리위의 무게에서 뺀다
#         window_value -= minus_val
#
#         if (window_value + truck) > l:
#             # 다리 위의 차 + 새로 진입하는 차의 무게가 l과 같거나 작아질 때 까지 팝한다.
#             while (window_value + truck) > l:
#                 minus_val = window.popleft()
#                 window_value -= minus_val
#                 window.append(0)
#                 ans.append(0)
#                 cnt += 1
#             window_value += truck
#             window.append(truck)
#             ans.append(truck)
#         else:
#             window_value += truck
#             window.append(truck)
#             ans.append(truck)
#
# print(len(ans))