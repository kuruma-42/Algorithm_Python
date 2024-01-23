# baekjoon 9498 시험 성적
# 조건문

a = int(input())

if 90 <= a and 100 >= a:
    print("A")
elif 80 <= a and 90 > a:
    print("B")
elif 70 <= a and 80 > a:
    print("C")
elif 60 <= a and 70 > a:
    print("D")
else:
    print("F")
