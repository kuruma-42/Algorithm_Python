# baekjoon 2525 오븐 시계 몸풀기
# 조리가 끝나는 시간을 출력하라
# 요리하는 데 필요한 시간 C ( 0<= C <= 1000) 분단위

t = list(map(int, input().split()))
h = t[0]
m = t[1]
c = int(input())

# 조리시간 + 분이 60 보다 적으면
if m + c < 60:
    m += c
# 조리시간 + 분이 60보다 크면
else:
    # 조리시간 분 합
    m += c
    # m을 60으로 나눈 몫을 구한다.
    p = m // 60
    # h에 p를 더해준다.
    h += p
    # 만약 h가 23 보다 크다면 h가 23 보다 작으면 그대로 출력
    if h > 23:
        h = h % 24
    # m을 60으로 나눈 나머지가 m이 된다.
    m = m % 60

print("{0} {1}".format(h, m))