'''
baekjoon 1244 스위치 켜고 끄기

남 -> 스위치 번호가 받은 수의 배수면 toggle
  -> % 연산을 통해 나머지가 0이면 배수가 된다

여 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭 가장 많은 스위치를 포함하는
구간을 찾아서 그 구간 스위치 상태 모두 바꾼다 구간 속에 속한 스위치의 개수는 항상 홀수

여
바꿔야 되는 인덱스를 리스트에 저장한 후
배열을 돌면서 모두 toggle 해준다.

스위치의 갯수 n 100개 이하

8
0 1 0 1 0 0 0 1
2
1 3
2 3

'''

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
t = int(sys.stdin.readline())
commands = []

for i in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    commands.append((x, y))

def reverse(idx: int):
    global arr
    if arr[idx]:
        arr[idx] = 0
    else:
        arr[idx] = 1

def boy(num: int):
    for i in range(num - 1, n):
        if (i + 1) % num == 0:
            reverse(i)

def girl(num: int):
    idx = num - 1
    reverse(idx)

    i = 1
    while idx - i >= 0 and idx + i < n:
        if arr[idx - i] == arr[idx + i]:
            reverse(idx - i)
            reverse(idx + i)
            i += 1
        else:
            break

for gender, num in commands:
    if gender == 1:
        boy(num)
    else:
        girl(num)

for i in range(n):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()