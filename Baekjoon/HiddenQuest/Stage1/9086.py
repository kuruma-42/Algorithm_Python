# baekjoon 9068 문자열 히든퀘스트
n = int(input())
arr = [input() for i in range(n)]

for i in arr:
    s = ""
    s += i[0]
    s += i[-1]
    print(s)


