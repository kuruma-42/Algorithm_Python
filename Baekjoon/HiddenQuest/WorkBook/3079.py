# baekjoon 3079 입국심사
# 친구 M명 (최대 10억명)
# K번 심사대에 앉아있는 심사관이 한 명을 심사하는데 걸리는 시간 Tk
# N입국 심사 10만 친구 10억명 친구만 선형탐색 해도 시간초과가 발생한다.
# 완전탐색으론 풀 수 없고, 그래프도 아니고, 선형적인 자료가 있는 투포인터도 아니고
# 그리디나 이진탐색으로 생각해볼 수 있다.
# 최대 시간이 걸리는 경우는 제일 많이 걸리는 곳에서 입국심사를 모두가 받는 경우다.
# 최대 최소 값 설정 잘하기
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
left = min(arr)
right = max(arr) * m
ret = right

# Check 함수를 잘 짜는 것이 이진 탐색에서 가장 중요하다.
def check(arr: [int], mid_val: int) -> bool:
    cnt = 0
    for i in range(n):
        # 주어진 시간에서 각 검사대가 끝낼 수 있는 최대 인원수 를 더해준다.
        cnt += mid // arr[i]

    # 친구의 숫자 보다 각 검색대에서 검사할 수 있는 최대 인원이 큰 경우 True 리턴
    if cnt >= m:
        return True
    # 아닌 경우는 False 리턴
    return False

while left <= right:
    # 중간  값을 구한다.
    mid = (left + right) // 2
    # 최대 시간 안에 끝낼 수 있으면
    if check(arr, mid):
        # 시간을 더 줄인다.
        right = mid - 1
        ret = min(ret, mid)
    else:
        # 시간안에 못 끝내면 시간을 늘린다.
        left = mid + 1

print(ret)

