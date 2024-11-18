class Node():
    def __init__(self):
        self.link = None
        self.data = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != None:
        current = current.link
        print(current.data,end=' ')
    print()


def insertData(findData,insertData):
    global pre,head,current,memory

    if head.data == findData: #첫번 째 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head #두번 째 삽입
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node() #마지막 삽입
    node.data = insertData
    current.link = node

def delData(delData):
    global pre,head,current,memory

    if head.data == delData: #첫 번째 노드 삭제
        current = head
        head = head.link
        del(current)
        return
    
    current = head # 두번 째 이후 노드 삭제
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delData:
            pre.link = current.link
            del(current)
            return
        

##전역변수 생성
memory  = []
pre,head,current = None,None,None
dataArray = ["다현","정현","쯔위","사나","지효"]

#메인코드 부분
if __name__ == "__main__":
    
    node = Node()   #첫번째 노드 생성
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:  #두번 째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    insertData("정현","홍권") 
    printNodes(head)

    insertData("재남","문별")
    printNodes(head)

    delData("문별")
    printNodes(head)