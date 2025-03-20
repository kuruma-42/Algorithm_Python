'''
baekjoon 3040 백설 공주와 일곱 난쟁이 (순열 itertools, bruteforce, impl)
9C7 -> 9C2로 생각해서 다양하게 풀어보기
'''

# import sys
#
# n = 9
# r = 2
# s = 0
# a: [int] = []
# total = 0
# result = []
#
# for i in range(0, n):
#     t = int(sys.stdin.readline())
#     total += t
#     a.append(t)


'''
재귀로 푼 경우 
'''
#
# import sys
#
# n = 9
# r = 2
# s = 0
# a: [int] = []
# total = 0
# result = []
#
# for i in range(0, n):
#     t = int(sys.stdin.readline())
#     total += t
#     a.append(t)
#
# def combination(n: int, r: int, start: int):
#     if len(result) == r:
#         key_logic(result)
#         return
#
#     for i in range(start, n):
#         result.append(a[i])
#         combination(n, r, i+1)
#         result.pop()
#
# def key_logic(arr: [int]):
#     if total - (arr[0] + arr[1]) == 100:
#         a.sort()
#         for j in a:
#             if j == arr[0] or j == arr[1]:
#                 continue
#             print(j)
#
# combination(n,r,s)

'''
itertools를 사용하는 방법
'''
#
# import sys
# import itertools
# n = 9
# a: [int] = []
# total = 0
#
# for i in range(0, n):
#     t = int(sys.stdin.readline())
#     total += t
#     a.append(t)
#
# # 7C2로 뽑는다
# nCr = itertools.combinations(a, 2)
#
# for j in list(nCr):
#     t = (j[0] + j[1])
#     if total - t == 100:
#         a.sort()
#         for k in a:
#             if k == j[0] or k == j[1]:
#                 continue
#             print(k)
