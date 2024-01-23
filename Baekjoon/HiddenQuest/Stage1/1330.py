# baekjoon 1330 두 수 비교하기 몸풀기
# 정수 비교 및 출력

t = list(map(int, input().split()))
a = t[0]
b = t[1]


if a > b:
    print(">")
elif a < b:
    print("<")
else :
    print("==")