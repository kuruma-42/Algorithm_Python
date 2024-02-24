from itertools import permutations
n = 6
r = 3
arr: [int] = [1,1,1,4,5,6]
result: [int] = []
isSelected: [int] = [0] * n

def permutation(n: int, r: int):
    if len(result) == r:
        print(result)
        return

    for i in range(n):
        if isSelected[i] == 1:
            continue

        result.append(arr[i])
        isSelected[i] = 1

        permutation(n, r)

        result.pop()
        isSelected[i] = 0

permutation(n,r)

# itertools를 사용한 방법
print(list(permutations(arr,r)))
for i in permutations(arr,r):
    print(i)


def doublepermutation(n: int, r: int):
    if len(result) == r:
        print(result)
        return

    for i in range(n):
        # if isSelected[i] == 1:
        #     continue

        result.append(arr[i])
        isSelected[i] = 1

        permutation(n, r)

        result.pop()
        isSelected[i] = 0

doublepermutation(n, r)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            print("i: {0}, j: {1}, k: {2}".format(i, j, k))
