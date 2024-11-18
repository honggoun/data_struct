def isQueueFull():
    global queue,front,rear,SIZE
    if((rear +1) % SIZE == front):
        return True
    else:
        return False

def isQueueEmpty():
    global queue,front,rear,SIZE
    if(front == rear):
        return True
    else:
        return False

def enQueue(data):
    global queue,front,rear,SIZE
    if(isQueueFull()):
        print("큐가 다 찼습니다")
        return
    rear = (rear+1)%SIZE
    queue[rear] = data

def deQueue():
    global queue,front,rear,SIZE
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global queue,front,rear,SIZE
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return
    return queue[(front+1)%SIZE]

SIZE = int(input("큐의 사이즈를 입력하세요-->"))
queue = [None for i in range(SIZE)]

if __name__ == "__main":
	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

while (select != 'X' and select != 'x'):
    if select == 'I' or select == 'i':
        data = input("입력할 데이터 ==> ")
        enQueue(data)
        print("큐 상태 : ", queue)
    elif select == 'E' or select == 'e':
        data = deQueue()
        print("추출된 데이터 ==> ", data)
        print("큐 상태 : ", queue)
    elif select == 'V' or select == 'v':
        data = peek()
        print("확인된 데이터 ==> ", data)
        print("큐 상태 : ", queue)
    else:
        print("입력이 잘못됨")

    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

print("프로그램 종료!")

