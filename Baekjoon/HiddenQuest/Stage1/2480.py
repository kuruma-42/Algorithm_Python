# baekjoon 2480 주사위 세개 몸풀기
# 같은 눈이 3개가 나오면 10000원 + (같은 눈) x 1000원의 상금을 받게 된다.
# 같은 눈이 2개면 1000원 + (같은 눈) x 100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) x 100원의 상금을 받게 된다.

t = list(map(int, input().split()))
a = t[0]
b = t[1]
c = t[2]
count = 0
ret = 0


def dice_sum3(a: int) -> int:
    return 10000 + (a * 1000)

def dice_sum2(a: int) -> int:
    return 1000 + (a * 100)

def dice_sum1(a: int) -> int:
    return 100 * a


# a b가 같을 때
if a == b:
    # a b c가 모두 같을 떄
    if b == c:
        ret = dice_sum3(a)
    # a b 만 같을 때
    else:
        ret = dice_sum2(a)

# b c가 같을 때
elif b == c:
    ret = dice_sum2(b)
# c a가 같을 때
elif c == a:
    ret = dice_sum2(c)
# 전부 다를 떄
else:
    t.sort()
    ret = dice_sum1(t[2])

print(ret)
