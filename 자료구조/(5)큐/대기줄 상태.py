def isQueueFull():
    global SIZE,queue,front,rear
    if(rear != SIZE-1):
        return False
    elif(rear == -1) and (front == -1):
        raise True
    else:
        for i in range(front+1,SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -=1
        rear -= 1

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("식당 영업 종료")
        return
    front +=1
    data = queue[front]
    queue[front] = None
    return data



queue = ["정국","뷔","지민","진","슈가"]
front = -1
rear = 4

for i in range(len(queue)+1):
    a = deQueue()
    print(a)
