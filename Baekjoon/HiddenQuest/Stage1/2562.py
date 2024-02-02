# baekjoon 2562 최댓값 몸풀기
arr: [int] = []
temp: [int] = []
for i in range(9):
    arr.append(int(input()))

temp = arr
temp.sort()
max_val = temp[8]

print(max_val)

for i in range(9):
    if arr[i] == max_val:
        print(i + 1)
        break