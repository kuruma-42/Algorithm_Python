# baekjoon 15552 빠른 A+B
import sys

n = int(input())
s = ""
for i in range(n):
    t = list(map(int, sys.stdin.readline().rstrip().split()))
    print(t[0] + t[1])

