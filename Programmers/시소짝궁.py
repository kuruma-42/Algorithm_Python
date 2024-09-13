'''
중심으로부터 2(m),3(m),4(m) 좌석
두 명이 마주보고 탄다
탑승한 사람 무게 x 축과의 거리의 곱이 같다면 시소 짝궁

일단 brute force로 풀어봄
시간 복잡도 때문에 어차피 안 되지만 시도해 봄

def solution(weights):
    answer = 0
    count = len(weights)
    for i in range(count):
        for j in range(count):
            if i != j:
                # 같은 수 비교
                if weights[i] == weights[j]:
                    answer += 0.5
                if weights[i] == weights[j] * 2:
                    answer += 1
                if weights[i] * 2 == weights[j] * 3:
                    answer += 1
                if weights[i] * 3 == weights[j] * 4:
                    answer += 1
                # 4배 4배 비교는 안 해도 됨 이유는 같은 수 비교와 같기 때문이다.
    return answer

Counter나 Dictionary를 사용해서 풀어야 함
Couter는 리스트의 성분이 어떻게 이뤄져있는 지 보여줌
하기와 같이 초기화 해서 쓸 수 있다.

from collections import Counter
Counter('HelloWorld')
# 출력: Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, 'W': 1, 'r': 1, 'd': 1})

상대와 나는 2와 3미터에 있을 수 있다.
예를 들어 -> 상대 * 3 = 나 * 2 이 맞는 수식이 있을 지 찾는다면
상대 = 나 * 3/2 가 있는 지를 생각해야한다.

Counter로 풀 수 있고
'''

from collections import Counter
def solution(weights):
    answer = 0
    weights = Counter(weights)
    print(weights)
    for w in weights:
        # 동일한 무게는 어차피 nC2니깐
        # 1:1 ex) 100 100
        answer += (weights[w] * (weights[w] - 1)) / 2
        # 2:3 ex) 180 270
        answer += weights[w] * weights[w * (3 / 2)]
        # 2:4 ex) 180 360
        answer += weights[w] * weights[w * (4 / 2)]
        # 3:4 ex) 270 360
        answer += weights[w] * weights[w * (4 / 3)]

    return answer
