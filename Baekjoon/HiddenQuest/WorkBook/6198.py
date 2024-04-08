# baekjoon 6198 옥상 정원 꾸미기
# n 건물 수
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
stk = []
ans = 0

for i in range(n):
    # 스택이 비어있지 않고 스택의 top의 값이 arr[i]의 값보다 작다면
    while stk and stk[-1] <= arr[i]:
        stk.pop()

    # 스택이 비어있거나, arr[i]의 값 보다 크다면
    stk.append(arr[i])
    # 스택에서 자기 자신을 뺀 후 답에 더해준다.
    ans += len(stk) - 1
print(ans)

# input = sys.stdin.readline
#
# n = int(input())
# q = []
#
# for i in range(n):
#     q.append(int(input()))
# cnt = 0
# height = 0
# for i in range(n):
#     for j in range(i,n):
#         # 첫 번째 인덱스
#         if i == j:
#             height = q[i]
#         else:
#             if q[j] >= height:
#                 break
#             else:
#                 cnt += 1
#
# print(cnt)