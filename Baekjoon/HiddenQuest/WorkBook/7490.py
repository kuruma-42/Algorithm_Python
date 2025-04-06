'''
baekjoon 7490 재귀 + 중복 순열로 풀어낸다.
n -> 1 부터 n 까지 오름차순으로 수열
'+' '-' 또는 ' '을 숫자 사이에 삽입 가능 (+-는 단순 연산, 공백은 숫자를 이어 붙인다. e.g. 2 3 => 23)
이렇게 넣어서 수식이 0이되는지 살펴본다.
N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램 작성하라

ASCII 순서에 따라 결과가 0이 되는 수식을 출력하라
각 테스트 케이스의 결과는 한 줄을 띄워 구분

ASCII 순서에 대해서 알아야 함
각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).
각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.

2
3
7

123456을 만들어야 함
eval을 알아야 함

'''

import sys
sys.setrecursionlimit(100000000)
t = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(t)]
ret = []
arr = []
ans = []

def combination(cnt):
    if cnt == 0:
        s = str(arr[0])
        for k in range(0, len(arr) - 1):
            s += ret[k]
            s += str(arr[k + 1])
        if eval(s.replace(' ','')) == 0:
            ans.append(s)
        return

    for op in ['+', '-', ' ']:
        ret.append(op)
        combination(cnt - 1)
        ret.pop()

# 테스트 케이스 돌린다.
for i in range(t):
    arr = [j for j in range(1, a[i] + 1)]
    combination(a[i] - 1)
    ans.sort()
    for element in ans:
        print(element)
    print()
    ans = []