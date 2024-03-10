# baekjoon 2217 로프
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때 각
# 각의 로프에는 모두 고르게 W/k 만큼의 중량이 걸리게 된다.
# 각 로프들에 대한 정보가 주어졌을 때 이 로프들을 이용하여 들어올릴 수 있는
# '최대' 중량을 구하는 프로그램을 작성하시요
# n은 100,000개 -> O(n^2)일 경우 터진다. (모든 로프를 사용할 필요가 없다?)
# 앞의 중량을 체크하는 것이 뒤의 선택에 영향을 미치지 않는다.
# 그리디 알고리즘 적용, 정렬이나 PQ를 사용한다.
#
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
ret = -1
# 오름차순으로 정렬
arr.sort(reverse=True)

for i in range(n):
    ret = max(ret, (i+1) * arr[i])

print(ret)

