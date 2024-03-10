# baekjoon 10828 스택
# 스택을 직접 구현하는 문제
import sys

n = int(sys.stdin.readline())
stk: [int] = []

for i in range(n):
    t = list(sys.stdin.readline().split())
    if t[0] == 'push':
       stk.append(t[1])
    elif t[0] == 'pop':
        if len(stk) == 0: print(-1)
        else: print(stk.pop(-1))
    elif t[0] == 'top':
        if len(stk) == 0: print(-1)
        else: print(stk[-1])
    elif t[0] == 'size':
        print(len(stk))
    elif t[0] == 'empty':
        if len(stk) == 0: print(1)
        else: print(0)
