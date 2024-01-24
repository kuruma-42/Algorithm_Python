# baekjoon 2884 알람시계
# 45분을 주어진 시간에서 빼면 된다.
# 조건문을 잘 써야한다.

t = list(map(int, input().split()))
h = t[0]
m = t[1]

# 분이 45보다 작으면
if m < 45:
    # 시간이 0이라면
    if h == 0:
        h = 23
        m = m + 60 - 45
    else:
        h -= 1
        m = m + 60 - 45
# 분이 45보다 크면
else:
    m = m - 45

print("{0} {1}".format(h,m))