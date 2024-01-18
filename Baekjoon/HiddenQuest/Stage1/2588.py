# baekjoon 2588 곱셈
# 세자리 X 세자리를 곱한다.

t = int(input())
arr = list(map(int, input()))

one = t * arr[2]
two = t * arr[1]
three = t * arr[0]
four = one + (two * 10) + (three * 100)

print(one)
print(two)
print(three)
print(four)
