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


size =7
stack = ["주황","초록","파랑","보라","빨강","노랑","과자집"]
top = 6

print("과자집에 가는 길:", end=" ")
for place in stack:
    print(place, end=" --> ")
    push(stack, place)  # 돌을 스택에 넣음
print("과자집")

# 집으로 돌아오는 길
print("우리집에 오는 길:", end=" ")
while stack:
    place = pop(stack)  # 스택에서 돌을 꺼냄
    if place != '과자집':
        print(place, end=" --> ")
    print("우리집")