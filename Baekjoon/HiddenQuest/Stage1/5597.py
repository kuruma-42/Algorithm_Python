# baekjoon 5597 과제 안 내신 분..?
n = 28
arr: [int] = [0] * 30
a = [int(input()) for i in range(n)]

for i in a:
    arr[i - 1] = 1

for j in range(30):
    if arr[j] == 0:
        print(j+1)
