# baekjoon 25304 영수증 몸풀기
total = int(input())
n = int(input())
ret = 0

for i in range(n):
    t = list(map(int, input().split()))
    ret += (t[0] * t[1])

if total == ret:
    print("Yes")

if total != ret:
    print("No")
