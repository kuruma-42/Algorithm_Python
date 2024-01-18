# baekjoon 10430 나머지
# (A+B)%C는 ((A%C) + (B%C))%C
# (A×B)%C는 ((A%C) × (B%C))%C
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

t = list(map(int, input().split()))


def print_mod(a: [int]):
    A = a[0]
    B = a[1]
    C = a[2]

    print((A + B) % C)
    print(((A % C) + (B % C)) % C)
    print((A * B) % C)
    print(((A % C) * (B % C)) % C)


print_mod(t)
