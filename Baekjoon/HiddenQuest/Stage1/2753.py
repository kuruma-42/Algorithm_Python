# baekjoon 2753 윤년 몸풀기
# 연도가 주어졌을 때 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하라
# 윤년은 4의 배수이면서, 100의 배수가 아낼때 또는 400의 배수일 때 이다.

t = int(input())

if t % 4 == 0:
    if t % 100 == 0:
        if t % 400 == 0:
            print("1")
        else:
            print("0")
    else:
        print("1")
else:
    print("0")
