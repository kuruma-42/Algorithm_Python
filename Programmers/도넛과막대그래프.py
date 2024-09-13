'''
도넛, 막대, 8자 그래프
1개 이상의 정점과 정점들을 연결하는 '단방향' 간선으로 이루어져있다.

도넛 -> 크기가 n인 도넛 그래프는 n개의 정점 n개의 간선
막대 -> 크기가 n인 막대 그래프 n개의 정점 n-1개의 간선
8자 -> 크기가 n인 8자 그래프 2n+1 정점 2n+2 간선

상기의 세 개의 그래프와 무관한 정점을 하나 생성한다. (무관하다 함은?)
각 도넛, 막대, 8자 그래프의 임의의 정점 하나로 향하는 간선들을 연결

정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를 구해야한다.

범위가 1,000,000 ?
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.

사고 과정

1. 도넛 모양 => 순환하면 도넛
2. 순환하지 않고 끝나면 막대
3. 동일한 정점이 순환을 두 번 하면 도넛
4. 탐색을 사용하려고 했는데, 범위가 100만이다. bfs, dfs만 재귀로 돌려도 터진다.
5. 연관이 없는 점이라 함은, 나가는 간선만 있고, 들어오는 간선이 없는 노드를 말한다?
    - 나가는 간선이 2개 이상이어야 함. 1개면 리프 노드
6. 이걸 탐색으로 알 수 있나..? 테이블이나 어딘가 메모를 한다?

'''


def solution(edges):
    answer = [0, 0, 0, 0]

    exchangeCnts = {}
    for a, b in edges:
        if not exchangeCnts.get(a):
            exchangeCnts[a] = [0, 0]
        if not exchangeCnts.get(b):
            exchangeCnts[b] = [0, 0]

        # 준 것, 받은 것 카운팅
        # a, b는 a가 b에 준 것, b가 a에게 받은 것
        exchangeCnts[a][0] += 1
        exchangeCnts[b][1] += 1

    for key, exchangeCnt in exchangeCnts.items():
        # 그래프는 최소 2개 이상으로 준 것만 2개 이상인 정점이 생성점
        if exchangeCnt[0] >= 2 and exchangeCnt[1] == 0:
            answer[0] = key
        # 받은 것만 있는 정점의 개수는 막대 그래프의 개수
        elif exchangeCnt[0] == 0 and exchangeCnt[1] > 0:
            answer[2] += 1
        # 준 것, 받은 것 각각 2개 이상인 점의 개수는 8자 그래프의 개수
        elif exchangeCnt[0] >= 2 and exchangeCnt[1] >= 2:
            answer[3] += 1

    # 전체 그래프 개수인 생성점의 준 것에서 2종류의 그래프를 빼면 도넛 그래프의 개수
    answer[1] = (exchangeCnts[answer[0]][0] - answer[2] - answer[3])

    return answer


