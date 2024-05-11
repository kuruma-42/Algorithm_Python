# baekjoon 13414 수강신청 (해쉬, 케이스워크)
# 수강 가능 인원 K (1 <= K <= 100,000)
# 대기 목록의 길이 L (1 <= L <= 500,000)
# O(n^2) 터진다
# 해쉬 값으로 잡을 것은 학번
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
possible = n
arr = []
ans = []
ret = ""

for i in range(m):
    dic[input().rstrip()] = i

ans = sorted(dic.items(), key=lambda x:x[1])

if n > len(ans):
    n = len(ans)

for i in range(n):
    print(ans[i][0])


# # 수강 가능인원이 대기 인원보다 크거나 같다면 모두 출력
# if n > m:
#     # 전원 출력
#     for _ in range(m):
#         print(input().rstrip())
#
# # 수강 가능인원이 대기 인원보다 작다면
# else:
#     for i in range(m):
#         dic[input().rstrip()] = i
#
#     ans = sorted(dic.items(), key=lambda x:x[1])
#
#     for i in range(n):
#         print(ans[i][0])
#


    #
    # for i in range(m):
    #     id = int(input())
    #     arr.append(id)
    #
    # arr.reverse()
    #
    # for id in arr:
    #     if dic.get(id) == None:
    #         dic[id] = 1
    #         ans.append(id)
    #
    # for i in range(n):
    #     print(ans.pop())




    # print(arr)
    # for i in range(1, m):
    #     id = int(input())
    #     if dic.get(id) == None:
    #         dic[id] = i
    #     else:
    #         dic[id] = i
    #
    # for key in dic.keys():
    #     if dic[key] <= m:
    #         if n == 0:
    #             break
    #         print(key)
    #         n -= 1