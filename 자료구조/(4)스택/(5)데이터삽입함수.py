def isStackFull():
    global SIZE,stack,top
    if(top >= SIZE-1):
        return True
    else:
        return False
    


#데이터 삽입함수
def push(data):
    global SIZE,top,stack
    if(isStackFull()):
        print("스택이 꽉 찼습니다")
        return
    else:
        top +=1
        stack[top] = data

SIZE = 5
stack = ["커피","녹차","꿀물","콜라",None]
top = 3

print(stack)
push("환타")
print(stack)
push("게토레이")

#스텍이 비어있는지 확인하는 함수
def isStackEmpty():
    global SIZE,stack,top
    if(top == -1):
        return True
    else:
        return False
    
SIZE = 5
stack = ["커피","녹차","꿀물","콜라",None]
top = -1

print("스택이 비었는지 여부 -->",isStackEmpty())

def pop():
    global SIZE,stack,top
    if(isStackEmpty()):
        print("스택이 비었습니다")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE,stack,top
    if(isStackEmpty()):
        print("스택이 비었습니다")
        return None
    return stack[top]

SIZE = 5
stack = ["커피",None,None,None,None]
top = 2

print(stack)
a = peek()
print("top의 데이터 확인 -->",a)
print(stack)