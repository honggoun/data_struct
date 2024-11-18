import random
class Node():
    def __init__(self):
        self.link = None
        self.data = None

def printNodes(start):
    current = start
    if current is None:
        return
    while current is not None:
        print(current.data, end=' ')
        current = current.link
    print()

def makeSimpleLinkedList(number):
    global memory, head, current, pre

    node = Node()
    node.data= number
    memory.append(memory)

    if head == None:
        head = node
        return
    
    if head.data>number:
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        current = current.link
        if current.data > number:
            break
    
    # 적절한 위치에 노드 삽입
    node.link = current.link
    current.link = node

memory = []
head, current, pre = None, None, None

# 로또 번호 생성 및 연결 리스트에 삽입
lottoNumbers = random.sample(range(1, 46), 6)  # 1~45 사이의 숫자 중 6개 랜덤 추출
lottoNumbers.sort()  # 정렬

for number in lottoNumbers:
    makeSimpleLinkedList(number)

# 결과 출력
printNodes(head)