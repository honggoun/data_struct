def isStackEmpty():
    global stack,top,size
    if(top == -1):
        return True
    else:
        return False

def isStackFull():
    global stack,top,size
    if(top>=size-1):
        return True
    else:
        return False

def push(data):
    global stack,top,size
    if(isStackFull()):
        print("스택이 가득 찼습니다")
        return
    top += 1
    stack[top] = data

def pop():
    global stack,top,size
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return
    data = stack[top]
    stack[top] = None
    top -=1
    return data

def peek():
    global stack,top,size
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return
    return stack[top]


size = int(input("사이즈를 입력하세요->"))
stack = [None for i in range(size)]
top = -1

if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 :", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 :", stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 :", stack)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
