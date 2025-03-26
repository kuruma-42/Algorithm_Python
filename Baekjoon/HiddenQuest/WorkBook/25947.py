'''
baekjoon 25947 선물 할인
n개의 선물 가격이 주어졌을 때, b의 예산으로 최대한 많은 선물을 사려고 한다.
이 때 a개의 선물에 대해서 반 값을 구할수 있다고 했을 때 최대로 살 수 있는 선물의 수를
구하는 프로그램을 작성하라. 단, 한 선물에는 최대 한 번만 반값 할인을 받을 수 있다.

선물의 개수 n,  (1 ≤ n ≤ 100,000)
예산 b  (1 ≤ n ≤ 10^9),
반값 할인을 받을 최대 선물의 개수 a

낮은 순으로 정렬
총 상품의 수에서 상품 개수로 이분 탐색을 한다.

이분 탐색으로 선택된 n까지의 합을 구간합을 구한다
구간합에서 할인 받을 선물의 개수 -a 까지의 구한다

해당 값이 예산 보다 크면 left를 mid + 1로 대체한다.
해당 값이 예산 보다 작으면 right를 mid - 1로 대체한다.
'''

import sys
n, b, a = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().strip().split(' ')))
prefix_arr = [0 for i in range(0, n)]
# 오름 차순 정렬
arr.sort()
ans = 0

# 누적합 구하기
def prefix_sum():
    for j in range(0, n):
        if j == 0:
            prefix_arr[j] = arr[j]
        prefix_arr[j] = arr[j] + prefix_arr[j - 1]

prefix_sum()

left = 0
right = len(arr)

def chk(cnt):
   idx = cnt - 1
   total_price = 0

   if cnt > a:
       sale_price = (prefix_arr[idx] - prefix_arr[idx - a]) / 2
       total_price = sale_price + prefix_arr[idx - a]
   else:
       total_price = (prefix_arr[idx] / 2)

   if b >= total_price:
       return True
   else:
       return False

while left <= right:
    mid = (left + right) // 2
    if chk(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)


# 로직 검토
# def chk(mid: int):
#     global ans
#
#     if mid <= a:
#         if b >= (prefix_arr[mid] / 2):
#             ans = mid
#             return True
#     else:
#         sale_price = (prefix_arr[mid - a] + ((prefix_arr[mid] - prefix_arr[mid - a]) / 2))
#         if b >= sale_price:
#             ans = mid
#             return True
#         else:
#             return False
#
#     if b >= prefix_arr[mid]:
#         ans = mid
#         return True
