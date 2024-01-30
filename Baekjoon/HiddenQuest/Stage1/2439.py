# baekjoon 2439 별찍기 - 2

n = int(input())
space = " "
star = "*"
for i in range(n):
    print("{0}{1}".format(space * (n - (i + 1)),star * (i + 1)))
