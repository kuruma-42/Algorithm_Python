# baekjoon 1744 수 묶기
# 길이가 N인 수열, 수열의 합을 구하려고 한다.
# 두 개의 수를 묶어서 곱해서 더한다 (두 수를 묶을 때 자기 자신을 묶지 못한다.)
# 한 번만 묶거나 묶지 않아야 한다.
# {0, 1, 2, 3, 4, 5}

"""
1.
- 오름 차순으로 정렬
- 맨 뒤에서 부터 pop을 2개 씩 한다.
- 그 수들을 묶어 준다.

- 음수, -1, 1 , 0 등에 대해서 예외처리 한다.
- 1은 더한다
- 제일 작은 음수 끼리 짝지어 곱하면 제일 크다
- 음수는 따로 뺀 다음에 0이 앞에 있었다면 저장했다가 곱해준다.
- 정상인 수는 차례대로 곱해준다.
"""
import sys

n = int(sys.stdin.readline())
arr = []
pair = []
one_count = 0
zero_count = 0
minus_arr = []
ret = 0
for i in range(0, n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

while arr:
    t = arr.pop()

# 1은 더하는 게 가장 크다
    if t == 1:
        one_count += 1
        continue

# 0은 마이너스와 짝을 지으면 가장 크다
    if t == 0:
        zero_count += 1
        continue

# 음수는 가장 작은 수만 남기고 0과 짝지어서 상쇄해야한다.
    if t < 0:
        minus_arr.append(t)
        continue

# 페어에 값이 들어있으면
    if len(pair) == 1:
        # 꺼내고
        c = pair.pop()
        # 곱해준다.
        ret += (t * c)
    else:
        # 페어에 값이 없으면 어펜드
        pair.append(t)

# 페어에 수가 남아있다면 더해서 끝낸다.
if pair:
    for p in range(0, len(pair)):
        ret += pair.pop()

# 1을 더해준다.
for k in range(0, one_count):
    ret += 1

# 음수 배열을 뒤집어서 제일 작은 수를 뒤로 놓는다.
minus_arr.sort(reverse=True)
while minus_arr:
    v = minus_arr.pop()
    if len(pair) == 1:
        # 꺼내고
        l = pair.pop()
        # 곱해준다.
        ret += (v * l)
    else:
        # 페어에 값이 없으면 어펜드
        pair.append(v)

for j in range(0, zero_count):
    if pair:
        pair.pop()

# 페어에 수가 남아있다면 더해서 끝낸다.
if pair:
    for e in range(0, len(pair)):
        ret += pair[e]

print(ret)
