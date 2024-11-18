class Node():
    def __init__(self):
        self.link = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != head:
        current = current.link
        print(current.data,end =' ')
    print()

def insertNode(findData,insertData):
    global head,pre,current,memory
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            pre.link = node
            node.link = current.link
            return
        node = Node()
        node.data = insertData
        node.link = head

def deleteNode(delData):
    global head,pre,current,memory
    if head.data == delData:
        current = head
        del(current)
        head = head.link
        while last.link != head:
            last = last.link
        last.link = head
    current = head
    while current != head:
        pre = current
        current = current.link
        if current.data == delData:
            


memory = []
head,pre,current = None,None,None
dataArray = ["다현","정연","쯔위","사나","지효"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre= head
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

