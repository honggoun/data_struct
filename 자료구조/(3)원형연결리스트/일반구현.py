class Node():
    def __init__(self):
        self.data = None
        self.link = None
        


def printNodes(start): #출력 함수
    current = start
    if current.data == None:
        return
    print(current.data,end=' ')
    while current.link != start:
        current = current.link
        print(current.data,end=' ')
    print()

def insertNode(findData,insertData):
    global pre,head,current,memory

    if head.data == findData: #첫번 째 데이터 삽입
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last != head:
            last = last.link
        last.link = node
        head = node
        return
    
    current = head #두번 째 이후 데이털 삽입
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            pre.link = node
            node.link = current
            return
        
        node = Node() #마지막 데이터 삽입
        node.dadta = insertData
        current.link = node
        node.link = head

def delData(delData):
    global pre,head,current,memory

    if head.data == delData: #첫번 째 데이터 제거
        current = head
        head = head.link
        last = head
        while last != head:
            last = last.link
        last.link = head
        del(current)
        return
    
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delData:
            pre.link = current.link
            del(current)
            return

def findData(fdata):
    global pre,head,current,memory

    current = head
    if current.data == fdata:
        return current
    while current.link != head:
        current = current.link
        if current.data == fdata:
            return current
    return Node()

#전역변수 선언
memory = []
pre,head,current = None,None,None
DataArray = ["다현","정연","쯔위","사나","지효"]

#메인 코드 부분
if __name__ == "__main__":

    node = Node() #첫번 째 생성
    node.data = DataArray[0]
    head = node
    node.link = node


    for data in DataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    insertNode("정연","추가데이터")
    printNodes(head)

    delData("추가데이터")
    printNodes(head)

    fdata = findData("재남")
    print(fdata.data)