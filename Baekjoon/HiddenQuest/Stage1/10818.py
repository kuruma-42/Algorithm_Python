# baekjoon 10818 최소,최대
n = int(input())
a = list(map(int, input().split()))
min_val = 987654321
max_val = -987654321

for i in a:
    min_val = min(min_val,i)
    max_val = max(max_val,i)

print("{0} {1}".format(min_val, max_val))