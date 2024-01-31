# baekjoon 10807 개수 세기 히든퀘스트
n = int(input())
a = list(map(int, input().split()))
f = int(input())
ret = 0

for i in a:
    if i == f:
        ret += 1

print(ret)