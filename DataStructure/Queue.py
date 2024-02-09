class Queue:
    def __init__(self):
        self.items = []         # 데이터 저장을 위한 리스트 준비
        self.front_index = 0    # 다음 dequeue될 값의 인덱스 기억

    def __len__(self):
        return len(self.items)

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):     # 이 기준이 동작하는 이유
            print("Queue is empty")
            return None     # dequeue할 아이템이 없음을 의미

        else: # dequeue는 front_index를 조정해서 삭제 효과를 얻음
            x = self.items[self.front_index]
            self.front_index += 1 # 다음에 dequeue될 값의 인덱스 조정
            return x

    def front(self): # deqeue 코드와 동일하지만 front_index를 증가시키는 코드만 없다.
        if self.front_index == len(self.items):
            print("Queue is empty")
            return None

        else:
            x = self.items[self.front_index]
            return x