# baekjoon 2562 최댓값 몸풀기
arr: [int] = []
max_val = -987654321

for i in range(9):
    t = int(input())
    max_val = max(max_val, t)
    arr.append(t)


print(max_val)

for i in range(9):
    if arr[i] == max_val:
        print(i + 1)
        break