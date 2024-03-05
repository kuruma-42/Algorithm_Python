# Binary Search 구현
# 탐색할 배열
arr = [1, 4, 7, 9, 11, 13, 16, 17, 21, 22, 25, 28]

# - Parameter key: 찾아야 하는 값
#             arr: 탐색할 배열
def binary_search(key: int, arr: [int]):
    # 오름차순으로 정렬
    arr.sort()
    # 첫 번째 인덱스를 왼쪽으로 잡는다.
    left = 0
    # 마지막 인덱스를 오른쪽으로 잡는다.
    right = len(arr) - 1

    # 왼쪽이 오른쪽 이하인 경우
    while left <= right:
        # 중간 값을 구한다. (괄호 꼭 잘 확인할 것)
        mid = int((left + right) / 2)
        # 만약 중간 값과 key값이 같다면
        if arr[mid] == key:
            # 출력
            print(mid)
            # 반복문 브레이크
            break
        # 만약 중간 값이 찾는 값 보다 크다면
        elif arr[mid] > key:
            # 오른쪽 값을 중간 - 1 값으로 설정 (mid도 탐색 범위가 아니기 때문)
            right = mid - 1
        # 만약 중간 값이 찾는 값 보다 작다면
        else:
            # 왼쪽 값을 중간 + 1 값으로 설정 (mid도 탐색 범위가 아니기 때문)
            left = mid + 1

binary_search(key=22, arr=arr)