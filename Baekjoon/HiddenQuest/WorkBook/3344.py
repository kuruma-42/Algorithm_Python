# baekjoon 3344 N-Queen 백트레킹
# 8x8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제
# 퀸은 같은 행,열,대각선의 말들을 공격할 수 있다.
# N-Queen은 파이썬으로는 baekjoon 3344에서는 시간초과가 난다.

n = int(input())
col = [0] * (n + 1)
cnt = 0

# parameter i: Depth
#           col: 칼럼 번호
def n_queen(i, col):
    global cnt
    # n은 column의 길이 빼기 1
    # 이유는 0 부터 시작하기 때문
    n = len(col) - 1
    # i 번째 댑스의 column을 가지고 promising 한지 확인
    if (promising(i, col)):
        # 만약 i와 n이 같다면 => 내가 모든 퀸을 프로미싱한 곳에 다 놓았다
        if (i == n):
            cnt += 1
            # 1번 칼럼부터 끝까지 출력
            print(col[1: n + 1])
        else:
            # 그렇지 않으면 다음 댑스의 1번 칼럼부터 끝까지 탐색
            for j in range(1, n + 1):
                # 1,2,3,4 ...n 번째에 퀸을 놔본다.
                col[i + 1] = j
                # 재귀 호출
                n_queen(i + 1, col)

# parameter i: Depth
#           col: 칼럼 번호
def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        # col[i] == col[k]의 의미는 같은 열에 있는지 체크하는 것이다.
        # abs(col[i] - col[k]) == (i - k) 대각선에 있는지 체크
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            # 퀸에게 위협 당한다면 False 처리
            flag = False
        # 인덱스를 증가시킨다.
        k += 1
    return flag

n_queen(0,col)
print(cnt)