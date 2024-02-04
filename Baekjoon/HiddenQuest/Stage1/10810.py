# baekjoon 10810 공넣기
# n은 바구니의 갯수, m은 공을 넣는 횟수

n,m = map(int, input().split(' '))
arr: [int] = [0] * n
for i in range(m):
   t = list(map(int, input().split(' ')))
   x1 = t[0] - 1
   x2 = t[1]
   v = t[2]

   for j in range(x1, x2):
      arr[j] = v

for i in arr:
   print(i, end=" ")