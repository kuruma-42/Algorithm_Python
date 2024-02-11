# baekjoon 10811 바구니 뒤집기
n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
for i in range(m):
    t = list(map(int, input().split()))
    f = t[0] - 1
    e = t[1]
    temp = arr[f:e]
    temp.reverse()

    for j in range(f, e):
        arr[j] = temp.pop(0)

for k in range(n):
    print(arr[k], end = " ")


