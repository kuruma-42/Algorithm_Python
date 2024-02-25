# Eratosthenes 소수 판독

# 정의에 충실한 단순 구현
# 가장 단순하고 비효율적인 방법
# 시간 복잡도 O(N)

def isPrimeV1(n: int) -> bool:
    if n == 1: return False
    if n == 2: return True

    for i in range(2,n):
        if n % i == 0: return False

    return True


import math
# 곱의 절반인 sqrt 까지만 반복
# 시간 복잡도 O(logN)

def isPrimeV2(n: int) -> bool:
    if n == 1: return False
    if n == 2: return True

    # math 라이브러리를 이용한 루트 계산
    end = int(math.sqrt(n))
    # 파이썬에서 기본적으로 루트를 하는 방식은 당연하게도 제곱(**)을 이용하는 방식이다.
    # end = int(n ** (1/2))

    for i in range(end):
        if n % i == 0: return False

    return True

# 에라토스테네스의 체

primes = []
def eratos(n: int):
    # idx = 해당수를 의미하고
    # arr[idx] = 1 이면 소수
    # arr[idx] = 0 이면 소수가 아님을 뜻한다
    # 초기화 - 모든 값을 1로 초기화 한다.
    # 0, 1은 소수가 아니다.

    arr = [1 for i in range(0, n + 1)]
    arr[0] = 0
    arr[1] = 0

    # 2..n 까지 반복
    for i in range(2,n):
        # 이미 0이면 건너 뜀.
        if arr[i] != 0: continue
        # 자신을 제외한 배수를 arr[idx] = 0 로 만들어 준다.
        for j in range(i+i, n, i):
            arr[j] = 0

    for i in range(2, n):
        if arr[i] != 0:
            primes.append(i)

eratos(10000)
print(primes)

