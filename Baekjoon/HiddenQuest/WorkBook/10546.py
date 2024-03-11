# baekjoon 10546 배부른 마라토너 (해쉬)
# 동명이인이 나올 수 있다.
# 딕셔너리는 중복키를 허용하지 않는다.
# 중복을 해결하려면 다른 자료구조를 쓰거나 해결책을 찾아야 한다.
# 참가자의 범위가 10^5라 O(n^2)으로 풀면 터진다.
# 해쉬값의 Value를 bool 형태 보다는 정수로 해 몇 명이 참가했고 몇 명이 완주했는지를 체크한다.

import sys
n = int(sys.stdin.readline())
runners_name = {}

for _ in range(n):
    t = sys.stdin.readline().rstrip()
    # 중복이 없는 경우
    if runners_name.get(t) == None:
        runners_name[t] = 1
    # 이미 참가자 목록에 있는 경우
    else:
        runners_name[t] = runners_name.get(t) + 1


for _ in range(n-1):
    t = sys.stdin.readline().rstrip()
    runners_name[t] = runners_name.get(t) - 1

for i in runners_name.keys():
    if runners_name[i] != 0:
        print(i)
