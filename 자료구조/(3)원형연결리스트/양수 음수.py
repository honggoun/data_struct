import random

class Node():
    def __init__(self):
        self.link = None
        self.data = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != head:
        current = current.link
        print(current.data, end=' ')
    print()

def countPosNeg():
    positive, negative = 0, 0

    if head == None:
        return positive, negative
    
    current = head
    while True:
        if current.data > 0:
            positive += 1
        elif current.data < 0:
            negative += 1
        elif current.data == 0:
            return

        if current.link == head:
            break
        current = current.link

    return positive, negative

def makePosNeg():
    current = head
    while True:
        current.data *= -1  # 양수는 음수로, 음수는 양수로 변환
        if current.link == head:
            break
        current = current.link


memory = []
pre, head, current = None, None, None

if __name__ == "__main__":
    # -100에서 100 사이의 7개의 난수 생성
    DataArray = []
    for i in range(7):
        DataArray.append(random.randint(-100, 100))

    # 첫 번째 노드 생성
    node = Node()
    node.data = DataArray[0]
    head = node
    node.link = head
    memory.append(node)

    # 두 번째 이후 노드 생성
    for data in DataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    # 양수, 음수 카운트
    pos_count, neg_count = countPosNeg()
    print("양수 -->", pos_count, '\t', "음수 -->", neg_count)

    # 양수는 음수로, 음수는 양수로 변환
    makePosNeg()

    # 변환된 리스트 출력
    printNodes(head)
