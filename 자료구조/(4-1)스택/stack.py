def isStackFull():
    global size,stack,top
    if(top>=size-1):
        return True
    else:
        return False

def push(data):
    global size,stack,top
    if(isStackFull()):
        print("스택이 다 찼습니다")
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global size,stack,top

    if(top == -1):
        return True
    else:
        return False
    
def pop():
    global size,stack,top
    if(isStackEmpty()):
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top -=1
    return data

def peek():
    global size,stack,top
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return None
    return stack[top]


size = 5
stack = ["커피","녹차","꿀물","콜라",None]
top = 3

push("홍권")
print(stack)

