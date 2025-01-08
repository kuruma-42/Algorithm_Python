'''
정수 배열 numbers
뒷 큰수 -> 자신보다 크고 자신과 제일 가까운 수 인덱스가 가까운 수
2,3,3,5 의 경우
큰 값이 없는 경우 -1을 넣는다.

투 포인터로 인덱스 계산?
백트래킹? 탐색중 끊어내야함.
자신의 값을 빼고 양수인 것 중 가 까운 값은 새로운 큐에 넣는다.
4 <= numbers <= 1,000,000 범위
O(n^2)이 나오면 터진다.

e.g.
    입력              출력
[2, 3, 3, 5]	[3, 5, 5, -1]
[9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1]
'''


# 테스트 19개 통과
# def solution(numbers):
#     idx1 = 0
#     idx2 = 0
#     arr = numbers
#     ret: [int] = []
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             t1 = arr[i]
#             t2 = arr[j]
#             # t2가 더 크면
#             if t1 < t2:
#                 ret.append(arr[j])
#                 break
#
#             # 마지막 인덱스 까지 큰 값이 없는 경우
#             if len(arr) - 1 == j:
#                 # -1 붙인다.
#                 ret.append(-1)
#     return ret


