# baekjoon 1253 좋다 (투포인터)
# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 "좋다(GOOD)"
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라
# 수의 위치가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.
# 수의 개수는 1<=N<=2000 값은 1,000,000,000
# 레프트 라이트가 존재한다. 포인터를 두 개 이상 사용해야한다.
# 정렬됐다는 말은 나오지 않는다.
# 선택된 수 보다 왼쪽 범위에서 이진 탐색이 진행되야 한다.
# ** 자기 쟈신을 제외해야한다 조심
import sys


n = int(sys.stdin.readline())
arr = list(map(int, input().rstrip().split(' ')))
ret = 0

arr.sort()

for selected_index in range(n):
    left_index = 0
    right_index = len(arr) - 1
    while left_index < right_index:
        if (arr[left_index] + arr[right_index]) == arr[selected_index]:
            if left_index == selected_index:
                left_index += 1
            elif right_index == selected_index:
                right_index -= 1
            else:
                ret += 1
                break
        elif (arr[left_index] + arr[right_index]) > arr[selected_index]:
            right_index -= 1
        else:
            left_index += 1

print(ret)