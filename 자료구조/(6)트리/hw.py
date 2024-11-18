class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# 이진 탐색 트리 생성
def insert_node(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root

# 중위 순회(in-order traversal) - 트리 내용을 출력
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

# 최소값을 찾는 함수 (삭제 시 대체할 노드를 찾기 위함)
def find_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# 노드 삭제 함수
def delete_node(root, data):
    if root is None:
        return root

    # 삭제할 데이터를 찾기 위한 탐색
    if data < root.data:
        root.left = delete_node(root.left, data)
    elif data > root.data:
        root.right = delete_node(root.right, data)
    else:
        # 자식 노드가 없는 경우 (리프 노드)
        if root.left is None and root.right is None:
            return None
        # 자식 노드가 하나인 경우
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # 자식 노드가 둘 다 있는 경우
        temp = find_min_value_node(root.right)  # 오른쪽 서브트리에서 최소값 노드 찾기
        root.data = temp.data  # 삭제할 노드에 최소값 복사
        root.right = delete_node(root.right, temp.data)  # 최소값 노드 삭제

    return root

# 트리 생성 및 데이터 삽입
root = None
nameAry = ["블랙핑크", "레드벨벳", "마마무", "에이핑크", "걸스데이", "트와이스"]
for name in nameAry:
    root = insert_node(root, name)

print("이진 탐색 트리 (중위 순회):")
inorder_traversal(root)
print("\n")

# 노드 삭제 (예: 마마무 삭제)
delete_name = "마마무"
print(f"'{delete_name}' 삭제 후:")
root = delete_node(root, delete_name)

# 삭제 결과 확인
inorder_traversal(root)
print()
