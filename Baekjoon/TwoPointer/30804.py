'''
baekjoon 30804 과일 탕후루 (Two Pointer)
꼬치는 최대 2가지 종류의 과일로 이루어 진다.
과일의 갯수는 200000개
O(n^2)일 경우 시간초과가 난다.

2가지 종류의 과일을 끼우고 있을 때
가장 길 때의 길이를 구하면 된다.

2종류 이상(3종류가 되는 시점)이 될 때는 끼운지 가장 오래된 종류를
2종류가 될 때 까지 빼준다.

5
5 1 1 2 1

3
1 1 1

9
1 2 3 4 5 6 7 8 9
'''

import sys

n = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split(' ')))

left = 0
max_length = 0
fruit_dict = dict()

for right in range(n):
    fruit = fruits[right]
    if fruit in fruit_dict:
        fruit_dict[fruit] += 1
    else:
        fruit_dict[fruit] = 1

    while len(fruit_dict) > 2:
        fruit_dict[fruits[left]] -= 1
        if fruit_dict[fruits[left]] == 0:
            del fruit_dict[fruits[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)

