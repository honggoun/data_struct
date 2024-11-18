import random
class Node():
    def __init__(self):
        self.link = None
        self.data = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != head:
        current = current.link
        print(current.data,end =' ')
    print()

def countOddEven():
    
    odd,even = 0,0

    if head == None:
        return
    current = head
    while True:
        if current.data % 2 == 0:
            even +=1
        else:
            odd +=1
        if current.link == head:
            break
        current = current.link
    
    return odd,even

def makeZeroNumber(odd,even):
    if odd > even:
        remainder = 1  # 홀수
    else:
        remainder = 0  # 짝수
        
    current = head
    while True:
        if current.data % 2 == remainder:
            current.data *= -1  # 홀수 또는 짝수에 해당하는 숫자를 음수로 변환
        if current.link == head:
            break
        current = current.link


memory = []
pre,head,current = None,None,None


if __name__ == "__main__":

    DataArray= []
    for i in range(7):
        DataArray.append(random.randint(1,100))

    node = Node()  #첫번째 노드 생성
    node.data = DataArray[0]
    head = node
    node.link = head
    memory.append(node)


    for data in DataArray[1:]:  #두번째 이후 노드 생성
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    oddcount,envecount = countOddEven()
    print("홀수-->",oddcount,'\t',"짝수-->",envecount)

    makeZeroNumber(oddcount,envecount)
    printNodes(head)