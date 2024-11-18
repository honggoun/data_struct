class Node():
    def __init__(self):
        self.link = None
        self.data = None

def printNnods(start):
    global pre,head,memory,current

    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current !=None:
        current = current.data
        print(current.data,end=' ')
    print()

def insertNode(findData,insertData):
    global pre,head,memory,current
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        node = Node()
        node.data = insertData
        pre.link = node
        node.link = current.link
        return
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(delData):
    global pre,head,memory,current
    if head.data == delData:
        current = head
        head = head.link
        del(current)
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delData:
            pre.link = current.link
            del(current)
        return

memory = []
head,pre,current = None,None,None
dataArray = ["다현","정연","쯔위","사나","지효"]

if __name__ =="__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)