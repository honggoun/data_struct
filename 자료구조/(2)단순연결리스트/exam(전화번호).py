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

def makeSimpleLinkdelist(namephone):
    global memory, head, current, pre

    node = Node()
    node.data = namephone
    memory.append(node)

    if head == None:
        head = node
        return
    
    if head.data[0]>namephone[0]:
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0]>namephone[0]:
            pre.link = node
            node.link = current
            return
    current.link = node

memory = []
head, current, pre = None, None, None

# Main code
if __name__ == "__main__":
    
    name = '_'
    while True:
        name = input("이름->>")
        if name != "":
            email = input("email->>")
            makeSimpleLinkdelist([name,email])
            printNodes(head)
        else:
            break