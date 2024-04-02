# baekjoon 17413 단어뒤집기 2 Stack
# 알파벳 소문자, 숫자, 공백, 특수문자 <>으로만 이루어짐
# 문자열의 시작과 끝은 공백이 아니다
# <가 등장하면 반드시 >가 등장하고 < 먼저 등장한다
# 태그는 <로 시작해서 >로 끝나는 길이가 3이상인 부분 문자열이다.
# < 와 > 사이에는 알파벳 소문자와 공백만 있다.
# < 와 >가 나오면 짝맞추기 문제 Stack 문제이다.
# s의 길이는 10만이다. O(n^2)이면 터진다.
# '<' 가 나왔을 때 그냥 전부 뺀다.
# '>' 가 나왔을 때 빼고 뒤집는다.
# 스택에 남아있는 값이 있는지 확인 후 뺸다.
# deque가 편해서 deque로 풀었다.
# if else 문이 많아져서 더 좋은 풀이를 생각해야겠다.
import sys
from collections import deque

input = sys.stdin.readline
s = list(map(str, input().rstrip()))
stk = []
q = deque()
ans = ""
is_open = False

for i in s:
    if i == "<":
        is_open = True
        while q:
          ans += q.pop()
        q.append(i)
    elif i == ">":
        is_open = False
        q.append(i)
        while q:
            ans += q.popleft()
    elif i == " ":
        if is_open:
            q.append(i)
        else:
            while q:
                ans += q.pop()
            ans += i
    else:
        q.append(i)

if q:
    while q:
        ans += q.pop()

print(ans)