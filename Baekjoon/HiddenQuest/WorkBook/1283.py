'''
baekjoon 1283 Simulation, String
한글 프로그램의 메뉴에는 총 N개의 옵션이 있다.
각 옵션들은 한 개 또는 여러 개의 단어로 옵션의 기능을 설명하여 놓았다.
그리고 우리는 위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 하였다.
단축키를 지정하는 법은 아래의 순서를 따른다.

먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다.
만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.
어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.
위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

첫째 줄에 옵션의 개수 N(1 ≤ N ≤ 30)이 주어진다.
둘째 줄부터 N+1번째 줄까지 각 줄에 옵션을 나타내는 문자열이 입력되는데 하나의 옵션은 5개 이하의 단어로 표현되며,
각 단어 역시 10개 이하의 알파벳으로 표현된다. 단어는 공백 한 칸으로 구분되어져 있다.

N 30개 단어 5개
1. 앞 단어가 등록이 안 되어있으면 맨 앞 단어를 등록
2. 모든 단어 첫 글자가 지정되어있다면 왼쪽에서 차례대로 알파벳을 보면서 단축키로 지정
3. 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자 구분 X
4. 위의 규칙을 첫 번째 부터 n번째 옵션까지 차례대로 적용한다

한 개 또는 여러 단어이다
Save As에서 S가 이미 단축키가 되었기 때문에 다음 단어인 As의 첫 단어인 A가 단축키가 된다
Save All은 양쪽 단어 첫 글자가 이미 등록되어있기 때문에 v가 단축키가 된다.


사용한 단축키를 넣을 배열을 만든다 (대소문자 2개 다 넣어주기)

# 1번조건 체크
옵션 각 단어의 첫 글자를 검사(split(‘ ‘)) 하고 단축키를 모아놓은 배열에 있는지 확인한다.

검사후 단축키를 찾음 => 단축키 지정후 (continue)
못 찾음 =>

#2번 조건
옵션의 모든 ‘케릭터 char’를 검사

검사후 단축키를 찾음 => 단축키 지정후 (continue)
못 찾음 =>

#3번 없음

5
New
Open
Save
Save As
Save All
'''

import sys

n = int(sys.stdin.readline())
arr = []
keys = []
answer = []

for i in range(0, n):
    t = sys.stdin.readline().rstrip().split(' ')
    arr.append(t)

for j in range(0,len(arr)):
    find_key_flag = False
    words = arr[j]
    for k in range(0, len(words)):
        word = words[k]
        lower = word[0].lower()
        upper = word[0].upper()
        if word[0] not in keys:
            keys.append(lower)
            keys.append(upper)
            find_key_flag = True
            arr[j][k] = word.replace(word[0], '[' + word[0] + ']', 1)
            break

    if find_key_flag:
        continue

    for k in range(0, len(words)):
        word = words[k]
        for p in range(1, len(word)):
            if word[p] not in keys:
                lower = word[p].lower()
                upper = word[p].upper()
                keys.append(lower)
                keys.append(upper)
                arr[j][k] = word.replace(word[p], '[' + word[p] + ']', 1)
                find_key_flag = True
                break

        if find_key_flag:
                break

for ans in arr:
    print(' '.join(ans))