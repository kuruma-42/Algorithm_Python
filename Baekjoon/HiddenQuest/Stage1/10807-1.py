# baekjoon 10807 개수 세기 히든퀘스트
# 카운트 활용 잘하기
n = int(input())
a = list(map(int, input().split()))
f = int(input())

ret = a.count(f)
print(ret)