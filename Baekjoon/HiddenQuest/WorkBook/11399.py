# baekjoon 11399 ATM 그리디
# ATM 1대
# 사람은 1번 부터 N번 까지 번호가 매겨져있따.
# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
# 작업 순서가 작은대로 정렬한다. 그리디 문제
# 그리고 누적합을 계산한다.
# 돈을 인출하는데 필요한 시간의 합을 '최소'로 만든다.
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
arr.sort()

t = 0
for i in arr:
    ans += i + t
    t += i

print(ans)