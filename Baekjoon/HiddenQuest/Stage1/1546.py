# baekjoon 1546 평균
# 자기 점수 중 최댓값을 고른 후
# 모든 점수를 점수/M*100으로 고친다.

n = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
ret = 0

for i in arr:
    ret += i / max_val * 100

ret /= n
print(ret)
