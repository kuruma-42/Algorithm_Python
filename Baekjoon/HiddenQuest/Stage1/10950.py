# baekjoon 10950 A+B - 3
# A B  입력 받고, A+B를 출력하는 프로그램을 작성하시오

n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    a = t[0]
    b = t[1]
    print(a+b)