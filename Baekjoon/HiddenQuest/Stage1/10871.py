# baekjoon 10871 X보다 작은 수
n,f = list(map(int, input().split()))
arr = list(map(int, input().split()))
s = ""
for i in arr:
    if i < f:
        s += "{0} ".format(i)

print(s)