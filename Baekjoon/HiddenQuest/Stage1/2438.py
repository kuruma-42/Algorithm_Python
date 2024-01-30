# baekjoon 2438 별찍기 - 1
# n 번째 줄에 별 n개를 찍는 문제

n = int(input())
star = "*"
for i in range(n):
    print(star * (i + 1))
