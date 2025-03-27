'''
baekjoon 15903 카드합체 놀이 (Greedy)

x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

첫 번째 줄에 카드의 개수를 나타내는 수 n(2 ≤ n ≤ 1,000)과 카드 합체를 몇 번 하는지를 나타내는 수 m(0 ≤ m ≤ 15×n)이 주어진다.
두 번째 줄에 맨 처음 카드의 상태를 나타내는 n개의 자연수 a1, a2, …, an이 공백으로 구분되어 주어진다. (1 ≤ ai ≤ 1,000,000)

가장 작은 수를 어떻게 만들지?
가장 작은 수 끼리 합치면 된다.
최대한 큰 수를 합치는 것을 마지막으로 미룬다.

4개의 수를 합체를 2번 진행한다.
pq에 4231을 작은 순으로 집어넣는다.

두 수를 팝한다
2가지를 더한다

값을 덮어 씌워준다.
다시 큐에 넣어준다.

4 2
4 2 3 1
'''

import sys
import heapq

n, m = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
ans = 0

# 힙 정렬
heapq.heapify(arr)

for _ in range(m):
    # 수 하나를 뺸다
    n1 = heapq.heappop(arr)

    if arr:
        # 수 하나를 뺸다
        n2 = heapq.heappop(arr)
        # 두 수를 더한다
        merged_value = n1 + n2
        # 배열에 추가한다
        arr += [merged_value, merged_value]
        # 다시 heap 정렬 한다
        heapq.heapify(arr)

# 총 합 계산
for value in arr:
    ans += value

print(ans)