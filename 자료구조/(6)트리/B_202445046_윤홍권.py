class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

def deleteNode(deleteName) :
    current = root
    parent = None
    while True:
        if deleteName == current.data :
            if current.left == None and current.right == None :   # 리프노드
                if parent.left == current :
                    parent.left = None
                else :
                    parent.right = None
                del(current)
                print("리프노드 : ", end = '')
            elif current.left != None and current.right == None :   # 왼쪽 노드
                if parent.left == current :
                    parent.left = current.left    
                else :
                    parent.right = current.left
                del(current)
                print("왼쪽 노드 : ", end = '')
            elif current.left == None and current.right != None :   # 오른쪽 노드
                if parent.left == current :
                    parent.left = current.right
                else :
                    parent.right = current.right
                del(current)
                print("오른쪽 노드 : ", end = '')
            elif current.left != None and current.right != None :   # 양쪽 노드
                change_node = current.right                    
                parent_change_node = current.right

                while change_node.left != None :
                    parent_change_node = change_node
                    change_node = change_node.left
                if change_node.right != None :       
                    parent_change_node.left = change_node.right
                else :
                    parent_change_node.left = None


                if deleteName < parent.data :
                    parent.left = change_node 
                else :
                    parent.right = change_node  

                change_node.left = current.left
                change_node.right = current.right 
                print("양쪽 노드 : ", end = '')
                    
                del(current)
                
            print(deleteName, '이(가) 삭제됨.')
            break

        elif deleteName < current.data :
            if current.left == None :
                print(deleteName, '이(가) 트리에 없음')
                break
            parent = current
            current = current.left
        else :
            if current.right == None :
                print(deleteName, '이(가) 트리에 없음')
                break
            parent = current
            current = current.right

def preorder(node) :
    if node == None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node) :
    if node == None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)
    
def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')

def printNode():
    print('전위 순회 : ', end = '')
    preorder(root)
    print('끝')

    print('중위 순회 : ', end = '')
    inorder(root)
    print('끝')

    print('후위 순회 : ', end = '')
    postorder(root)
    print('끝')

## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['31', '15', '13',  '18', '11', '14', '16', '19', '17', '41', '35', '33', '37','48', '43', '51', '44']

## 메인 코드 부분 ##
if __name__ == "__main__" :
    node = TreeNode()
    node.data = nameAry[0]
    root = node
    memory.append(node)

    for name in nameAry[1:] :
        node = TreeNode()
        node.data = name

        current = root
        while True :
            if name < current.data :
                if current.left == None :
                    current.left = node
                    break
                current = current.left
            else :
                if current.right == None :
                    current.right = node
                    break
                current = current.right

        memory.append(node)

    printNode()
    deleteNum = input('삭제 번호 입력-->')

    while (deleteNum != '-1') :
        deleteNode(deleteNum)
        printNode()
        deleteNum = input('삭제 번호 입력-->')

    print("프로그램 종료!")
