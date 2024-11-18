

def isQueueFull():
    global SIZE,queue,front,rear
    if(rear == SIZE-1):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print("큐가 가득 찼습니다")
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return
    return queue[front+1]

SIZE = int(input("큐의 사이즈를 정하시오"))
queue = [None for i in range(SIZE)]
front=rear=-1

select = -1

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