'''
Baekjoon 14921 용액 합성하기
- -100000000 ~ 100000000 (특성 값이 0)
- 2<= N <= 100000 O(n^2) 되면 터짐
- 탐색을 하는데 투포인터를 써서 탐색해야함.
- 0에 가깝게 만들기 ..?
- 레프트 인덱스가 움직이는 조건 0보다 작으면
- 오른쪽 인덱스가 움직이는 경우 0보다 크면
- 왼쪽과 오른쪽을 더한 값을 양수면 0에서 더하고 음수면 빼서 크기를 비교 X
- 위의 말이 절대 값이랑 똑같음
'''

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split(' ')))

idx1 = 0
idx2 = n - 1
ret = arr[idx1] + arr[idx2]

while idx1 < idx2:
    # 두 수를 더한다
    t = arr[idx1] + arr[idx2]

    # 이전 값 보다 새로운 값이 더 작다면
    if abs(ret) > abs(t):
        ret = t

    # 오름차순으로 정렬되어있다는 것을 기억한다.
    # 두 수를 더한 값이 0보다 작으면
    if t < 0:
        # 왼쪽 인덱스를 당겨준다.
        idx1 += 1
    # 두 수를 더한 값이 0보다 크면
    else:
        # 오른쪽 인덱스를 내림
        idx2 -= 1

print(ret)


