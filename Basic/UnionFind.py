
v, e = (6,7)
table = [i for i in range(v + 1)]

# 해당
def get_parnet(n):
    # 대표값이 노드의 번호와 같다면 대표 값이다.
    if n == table[n]:
        return n
    # 대표값이 노드의 번호와 다르다면
    else:
        # 재귀의 형태로 get_parnet()를 불러준다.
        table[n] = get_parnet(table[n])
        # 재귀가 다 돌면 부모를 찾을 수 있다.
        return table[n]

# 원소 a와 원소 b를 같은 집합으로 한다.
def union(a, b):
    # a의 부모를 찾는다.
    ap = get_parnet(a)
    # b의 부모를 찾는다.
    bp = get_parnet(b)

    # 만약 a의 부모보다 b의 부모가 작다면
    if ap < bp:
        # bp의 대표 값은 ap가 된다.
        table[bp] = ap
    else :
        # ap의 대표 값은 bp가 된다.
        table[ap] = bp

# 원소 a와 원소 b가 같은 집합인지 확인한다.
def find(a, b):
    # 둘의 부모를 확인했을 때 값이 같다면 같은 집합이다.
    return get_parnet(a)