'''
baekjoon 2407 조합
5<=n<=100, 5<=m<=100, m <= n
nCm을 출력하라
nCr = n-1Cr-1 + n-1Cr
DP를 이용한 조합.
Table[n][r] 상향식 DP로 생성해보기

* 배울점 제한 사항을 잘 확인하지 않아서
DP로 풀 생각을 못함, 단순 콤비로 풀어서 시간 초과가 남
'''

import sys
input = sys.stdin.readline

n, r = map(int, input().split(' '))

result: [int] = []
count = 0

def combination(n: int, r: int, start: int):
    global count
    if len(result) == r:
        count += 1
        return

    for i in range(start,n):
        result.append(i)
        combination(n,r,i+1)
        result.pop()

combination(n,r,0)

print(count)