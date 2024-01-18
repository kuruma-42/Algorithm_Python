# baekjoon 18108 1998년생인 내가 태국에서는 2541년생?! (몸풀기)
# 2541 -> 1998
# 불기 연도를 서기 연도로 변환한 결과를 출력한다.
# 불기 연도에서 516을 빼면 서기 연도가 나온다.

t = int(input())


def cal_budi(a: int) -> int:
    return a - 543


print(cal_budi(t))

