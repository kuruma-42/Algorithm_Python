# baekjoon 11501 주식
# 세 가지 행동을 함
# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안 한다.
# 날별로 주식의 가격을 알려주었을 때 '최대'의 이익이 얼마나 되는지 계산
# N은 2<= N <=1,000,000 (O(N^2))돌면 터진다.
# 팔아야 하는 조건은 산 값 보다 낮을 때
# 이득이 아예 없는 조건은 산 값이 제일 높은 날.
# 아무것도 안 하는 날 어떤 날일까? (산 가격 보다 낮은 날 마지막 날 손해를 보는 날)
# 마지막날 전 가격이 마지막 날 보다 크면 아무 것도 안 한다.
# 이득이 생길 때 무조건 팔고 가지고 있고를 계산한다? 부분 부분 마다
# 제일 비싼 날 보다 싼 날 다 사서 제일 비싼날 다 판다.
# 재귀로 푼다
# 재귀로 풀면 88%에서 메모리 초과남
# 거꾸로 뒤집으면 쉽게 해결됨.

T = int(input())

for t in range(T):

    N = int(input())
    price = list(map(int, input().split()))

    money = 0 # 이익

    maxPrice = 0 # 주식의 최대 가격
    for i in range(len(price)-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else: # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
            money += maxPrice - price[i]

    print(money)

'''
88%에서 메모리 초과난 풀이 
import sys

    def go(temp: [int]):
        cnt = 0
        wage = 0
        if len(temp) == 0:
            return

        global benefit

        max_val = max(temp)
        idx = temp.index(max_val)

        for i in range(0, len(temp)):
            # 최댓값 보다 작으면
            if max_val > temp[i]:
                # 주식의 갯수 더해준다. (최대 이득을 계산할 때 쓰임)
                cnt += 1
                # 주식을 산 비용을 더해준다.
                wage += temp[i]
            # 최댓값이 있는 인덱스라면
            if i == idx:
                # 최대 판매가 계산
                max_sale_price = cnt * temp[i]
                # 최대 이득 계산 ( 최대 판매가 - 비용 )
                benefit += (max_sale_price - wage)
                break

        go(temp[idx+1:])

    input = sys.stdin.readline
    t = int(input())
    benefit = 0

    for i in range(t):
        n = int(input())
        z = list(map(int, input().split()))
        go(z)
        print(benefit)
        benefit = 0

'''

