# baekjoon 1874 스택 수열 (Stack)
# 스택에 push하는 순서는 오름차순을 지킨다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열을 만들 수 있다.
# 임의의 수열이 주어졌을 때 수열을 만들 수 있는지 없는지 판별 하고
# 어떤 순서로 push pop 연산을 수행할 수 있는지 알아내는 프로그램을 작성하라.
import sys
input = sys.stdin.readline
n = int(input())
t = [i for i in range(1,n+1)]
arr = [int(input()) for i in range(n)]

stk = []
ans = []
ret = []

t = list(reversed(t))
arr = list(reversed(arr))

while True:
    # 스택이 비어있지 않다면
    if stk:
        # arr의 탑과 스택의 탑이 같지 않다면
        if arr[-1] != stk[-1]:
            # 주어진 연속된 수가 비어있지 않다면
            if t:
                # 스택에 넣어주고
                ret.append("+")
                # 연속된 수에서는 빼준다.
                stk.append(t.pop())
            # 주어진 연속된 수가 비어있으면
            else:
                # 만들 수 없는 것이다.
                print("NO")
                # 브레이크
                break

        # arr의 탑과 t의 첫 번째가 같다면
        else:
            # 정답에 stk에서 팝 한 값을 넣어준다.
            ans.append(stk.pop())
            # 정답 예시에서도 팝
            arr.pop()
            # 출력 결과 어팬드
            ret.append("-")

    # 스택이 비어있다면
    else:
        # t가 비어있지 않다면
        if t:
            # 출력 결과 어팬드
            ret.append("+")
            # 연속된 수에서도 팝해준다.
            stk.append(t.pop())
        # t가 비어있다면
        else:
            # 정답 출력
            for i in ret:
                print(i)
            break

