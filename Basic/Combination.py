from itertools import combinations
n = 6
r = 3
arr: [int] = [1,2,3,4,5,6]
result: [int] = []

def combination(n: int, r: int, start: int):
    if len(result) == r:
        print(result)
        return

    for i in range(start,n):
        result.append(i)
        combination(n,r,i+1)
        result.pop()

combination(n,r,0)


def combination_iterator(n: int, r: int):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                print("i: {0}, j: {1}, k: {2}".format(i, j, k))


combination_iterator(n,r)

# itertools를 사용하면 combination을 쓸 수 있다.
# 갯수
print(combinations(arr,3))

# 경우의 수 출력
for i in combinations(arr,3):
    print(i)