'''
Programmers 숫자변환하기 탐색 BFS

자연수 x -> y로 변환.
사용가능 연산 세 가지
x + n
x * 2
x * 3

BFS로 최단거리를 구하고
못 찾으면 -1 리턴

Review
BFS 기본 구조 잘못 씀
변수명을 내가 맞는 상황에 깔끔하게 못적음
e.g. i,j
기본적인 띄어쓰기 컨벤션을 넣어야 함
가독성이 떨어지니 사소로운 실수가 나옴
'''

# from collections import deque
# 해당 풀이는 방문체크 시기를 잘못해서 중복이 많이 발생해서 시간초과 두 개를 통과하지 못했다.
#
# def solution(x, y, n):
#     ans = deque()
#     ans.append((x,0))
#     visited = set()
#     while ans:
#         # x와 차수를 선택
#         i,j = ans.popleft()
#         # 백 트레킹
#         if i > y:
#             continue
#         # 방문 체크
#         if y in visited:
#             continue
#         # 찾는 값이 나오면 j return
#         if i == y:
#             return j
#         # 방문 처리
#         visited.add(i)
#
#         for idx in range(3):
#             if idx == 0:
#                 # 더하기 n
#                 if i + n <= y and i + n not in visited:
#                     ans.append((i+n, j+1))
#             if idx == 1:
#                 # 곱하기 2
#                 if i * 2 <= y and i * 2 not in visited:
#                     ans.append((i*2, j+1))
#             if idx == 2:
#                 # 곱하기 3
#                 if i * 3 <= y and i * 3 not in visited:
#                     ans.append((i*3, j+1))
#     # while이 끝난 경우는 답이 없는 경우
#     return -1


#
# from collections import deque
#
#
# def solution(x, y, n):
#     ans = deque()
#     ans.append((x, 0))
#     visited = set()
#     visited.add(x)
#
#     while ans:
#         # x와 차수를 선택
#         i, j = ans.popleft()
#
#         # 찾는 값이 나오면 j return
#         if i == y:
#             return j
#
#         for idx in range(3):
#             if idx == 0:
#                 # 더하기 n
#                 if i + n <= y and i + n not in visited:
#                     ans.append((i + n, j + 1))
#                     visited.add(i + n)
#
#             if idx == 1:
#                 # 곱하기 2
#                 if i * 2 <= y and i * 2 not in visited:
#                     ans.append((i * 2, j + 1))
#                     visited.add(i * 2)
#
#             if idx == 2:
#                 # 곱하기 3
#                 if i * 3 <= y and i * 3 not in visited:
#                     ans.append((i * 3, j + 1))
#                     visited.add(i * 3)
#
#     # while이 끝난 경우는 답이 없는 경우
#     return -1

from collections import deque


def solution(x, y, n):
    ans = deque()
    ans.append((x, 0))
    visited = set()

    while ans:
        i, j = ans.popleft()
        # 백 트레킹 or 방문 체크
        if i > y or y in visited:
            continue
        # 방문 처리
        visited.add(i)
        # 찾는 값이 나오면 j return
        if i == y:
            return j

        for k in (i * 3, i * 2, i + n):
            if k <= y and k not in visited:
                ans.append((k, j + 1))

    # while이 끝난 경우는 답이 없는 경우
    return -1

