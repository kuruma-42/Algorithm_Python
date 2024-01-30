# baekjoon 10952 A+B - 5

while True:
    t = list(map(int, input().split()))
    if t[0] == 0 and t[1] == 0:
        break
    print(t[0] + t[1])