# baekjoon 1026 보물 (그리디)
# 길이가 N 정수 배열 A와 B가 있다.
# S = A[0] x B[0] + .... + A[N-1]xB[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자.
# 단, B에 있는 수는 재배열하면 안 된다.
# 첫쨰 줄에 N이 주어진다.
# A를 정렬 오름차순 정렬, B를 내림 차순 정렬 후 곱하면 최저값이 구해진다.
# 재배열이 불가능하다고 하지만, 출력 값은 어쨌든 최소 합이다.

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
ret = 0
a.sort()
b.sort(reverse=True)
for i in range(n):
    ret += (a[i] * b[i])

print(ret)