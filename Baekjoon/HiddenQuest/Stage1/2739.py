# baekjoon 2739 구구단
# N단을 출력하는 프로그램 작성

n = int(input())

for i in range(1,10):
    print("{0} * {1} = {2}".format(n, i, n*i))