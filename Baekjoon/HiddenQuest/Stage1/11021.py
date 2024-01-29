# baekjoon 11021 A+B - 7
import sys

n = int(input())

for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    print("Case #{0}: {1}".format(i+1, t[0] + t[1]))

