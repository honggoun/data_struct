class Node() :
    def __init__ (self) :
        self.plink = None            # 앞쪽 링크
        self.data = None
        self.nlink = None 

def printNodes(start) :
    current = start
    if current.link == None:
        return
    print("정방향-->",end=' ')
    print(current.data,end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data,end =' ')
    print()
    print("역방향-->",end=' ')
    print(current.data,end = ' ')
    while current.plink != None:
        current = current.plink
        print(current.data,end=' ')
    print()

def insertNodes(findData,insertData):
    global memory,pre,head,current
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.nlink = head
        node.plink = node
        head = node
        return
    current = head
    while current.nlink == None:
        pre = current
        current = current.nlink
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.nlink = head
            head.plink = node
            head = node 
            return
        current = head
        while current.nlink != None:
            pre = current
            current = current.nlink
            if current.data == findData:
                node = Node()
                node.data = insertData
                node.nlink = current
                current.plink = node
                pre.nlink = node
                node.plink = pre
                return
        node = Node()
        node.data = insertData
        current.nlink = node
        node.plink = current

def deletNode(delData):
    global memory,pre,head,current

    if head.data == delData:
        current = head
        head = head.nlink
        head.plink = None
        del(current)
        return
    current = head
    while current.nlink != None:
        pre = current
        current = current.nlink
        if current.data == delData:
            pre.nlink = current.nlink
            if current.data == None:
                current.nlink.plink = pre
            del(current)
            return



memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]