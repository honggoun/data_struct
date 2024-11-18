class Node():
    def __init__(self):
        self.link = None
        self.data = None

##함수 선언##
def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != head:
        current = current.link
        print(current.data,end =' ')
    print()

def insertData(findData,insertData):
    global memory,pre,current,head

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        while last.link != head:
            last = last.link
        last.link = node
        node = head
        return
    current = head
    while current.link != head:
        pre = current
        current = current.link
        node = Node()
        node.data = insertData
        node.link = current
        pre.link = node
        return
    node = Node()
    current.link = node
    node.link = head

def deleteData(delData):
    global memory,pre,current,head

    if delData == None:
        return
    if head.data == delData:
        current = head
        head = head.link
        last = head
        while last.link != current:
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
    global memory,pre,current,head

    current = head
    if current.data == fdata:
        return current
    while current.link != head:
        current = current.link
        if current.data == fdata:
            return current
    return Node()


##전역변수 선언##
memory = []
pre,head,current = None,None,None
DataArray = ["다현","정연","쯔위","사나","지효"]

##메인함수##

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

insertData("쯔위","홍권")
deleteData("홍권")
deleteData("지효")
printNodes(head)
a = findData("쯔위")
print(a.data)