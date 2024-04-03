# baekjoon 1541 잃어버린 괄호 (Greedy)
# 문자열 길이 50이다. 완전 탐색 가능
# -로 먼저 자른다.
# -로 잘린 배열은 + 값만 있을 것이다.
# +로 split후 모두 더한 후 뺴주면 최소 값이 된다.
# 괄호 구간의 선택이 다음 구간의 선택에 영향을 주지 않는다.
# 구간을 선택해서 더할수록 계산해야하는 범위가 줄어든다.
# 기법만 생각하면 자료형을 쓰지 않고 완탐으로 풀 수 잇는 문제

import sys
input = sys.stdin.readline

s:[str] = list(map(str, input().rstrip().split('-')))
ans = 0

for i in range(len(s)):
    # i가 처음이면 더해준다.
    if i == 0:
        temp_arr = list(map(str, s[i].rstrip().split('+')))
        t = 0
        for j in temp_arr:
            t += int(j)
        ans += t
    else:
        if i == '':
            continue
        else:
            temp_arr = list(map(str, s[i].rstrip().split('+')))
            t = 0
            for j in temp_arr:
                t += int(j)
            ans -= t

print(ans)