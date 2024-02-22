from itertools import permutations
n = 6
r = 3
arr: [int] = [1,2,3,4,5,6]
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

# permutation(n,r)

# itertools를 사용한 방법
# print(list(permutations(arr,r)))
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

doublepermutation(n,r)