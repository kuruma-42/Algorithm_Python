'''
baekjoon 1920 수 찾기 (이분탐색)
N(1 ≤ N ≤ 100,000)
M(1 ≤ M ≤ 100,000)
 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.
 O(n^2) 나오면 터진다.
 이분 탐색으로 푸는 게 좋다.
'''
import sys

n = int(sys.stdin.readline())
find_arr = list(map(int, sys.stdin.readline().split(' ')))
m = int(sys.stdin.readline())
target_arr = list(map(int, sys.stdin.readline().split(' ')))
# 찾을 곳 정렬
find_arr.sort()

for target_value in target_arr:
    left_idx = 0
    right_idx = len(find_arr) - 1
    find_flag = False
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        # 찾은 경우
        if target_value == find_arr[mid_idx]:
            print(1)
            find_flag = True
            break
        # 찾으려는 값 보다 중간 값이 작은 경우
        elif target_value > find_arr[mid_idx]:
            left_idx = mid_idx + 1
        # 찾으려는 값 보다 중간 값이 큰 경우
        else:
            right_idx = mid_idx - 1
    if find_flag == False:
        print(0)