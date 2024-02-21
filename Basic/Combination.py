n = 6
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

combination(n,3,0)




