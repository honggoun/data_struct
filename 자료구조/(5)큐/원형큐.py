def isQueueFull():
    global queue,front,rear,SIZE
    if((rear+1)%SIZE==front):
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
