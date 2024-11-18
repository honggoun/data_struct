##함수 선언##
class Node():
    def __init__(self):
        self.link = None
        self.data = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link   != None:
        current = current.link
        print(current.data,end=' ')
    print()

def insert_Data(findData,insertData):
    global memory,pre,head,current

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            pre.link = node
            node.link = current
            return
    node = Node()
    node.data = insertData
    current.link = node

def delet_Data(findData):
    global memory,pre,head,current

    if head.data == findData:
        current = head
        head = head.link
        del(current)
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:    
            pre.link = current.link
            del(current)
            return


##전역변수 선언##
memory = []
head,pre,current = None,None,None
dataArray = ["다현","정연","쯔위","사나","지효"]

##메인함수##
if __name__ == "__main__":

    node = Node()   #첫번째 노드 생성
    node.data = dataArray[0]
    head = node
    memory.append(node)


    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
        