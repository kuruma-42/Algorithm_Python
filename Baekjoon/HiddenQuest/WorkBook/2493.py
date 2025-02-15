'''
baekjoon 2493 탑
입력
5
6 9 5 7 4

결과
0 0 2 2 4

N은 1 이상 500,000 이하이다.

O(n^2) 나오면 터진다

마지막꺼 큰 거 나올 때 까지 계속 팝한다.
팝하고 집어넣는다.
'''

n = int(input())
heights = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n):
    # 핵심 코드
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)

''' 
하기의 코드는 시간초과 나는 코드 O(n^2)
문제에서 나타내는대로 그대로 물리적으로 
스택에 넣고 뺴고 하게 구현하면 제한 시간 내에 구현이 불가하다. 
해당 문제는 모노 스택을 이용해서 풀어야 한다.

import sys
import copy

n = int(sys.stdin.readline())
stk = list(map(int, sys.stdin.readline().split()))
stk_copy = copy.deepcopy(stk)
ret = [0 for i in range(0, n)]
print(n)
print(stk)
print(ret)

while True:
    # 아무것도 없으면 break
    if len(stk) == 0:
        break
    pop_idx = len(stk) - 1
    # 실제 스택에서 뺴주고
    stk_pop = stk.pop()
    # 복사본에서도 빼준다.
    stk_copy.pop()
    for i in range(0,len(stk)):
        # 탑의 값이 스택에 뺀 값 보다 크면 위치 인덱스 기록
        if stk_copy[-1] >= stk_pop:
            ret[pop_idx] = len(stk_copy)
            break
        else:
            stk_copy.pop()
    stk_copy = copy.deepcopy(stk)

print(ret)
'''