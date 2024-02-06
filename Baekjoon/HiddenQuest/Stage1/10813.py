#baekjoon 10813 공바꾸기
# 1부터 N번까지 번호가 매겨져 있다.
# M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택한다.
# 두 바구니에 들어있는 공을 서로 교호나한다.
# 공을 어떻게 바꿀지가 주어졌을 때 공을 M번 바꾼 이후에 어떤 공이 있는지 구하시오

n,m = map(int, input().split())
arr: [int] = []
for i in range(n):
    arr.append(i+1)

for j in range(m):
    t,z = map(int, input().split())
    arr[t - 1],arr[z - 1] = arr[z - 1],arr[t - 1]

for i in range(n):
    print(arr[i], end = " ")
    

# 조금 더 짧은 풀이
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
buckets = list(range(1, N+1))
for _ in range(M):
  a, b = map(int, input().split())
  buckets[a-1], buckets[b-1] = buckets[b-1], buckets[a-1]
print(' '.join(map(str, buckets)))
'''
