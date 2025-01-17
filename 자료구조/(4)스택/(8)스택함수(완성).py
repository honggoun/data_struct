##함수 선언 부분##
def isStackFull():
    global size,top,stack

    if top >= size-1:
        return True
    else:
        return False

def isStackEmpty():
    global size,top,stack
    if top == -1:
        return True
    else:
        return False
    
def push(data):
    global size,top,stack

    if(isStackFull()):
        print("스택이 다 찼습니다")
        return
    top += 1
    stack[top] = data

def pop():
    global size,top,stack
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global size,top,stack
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return
    return stack[top]

##전역함수 선언##
size = int(input("스택의 사이즈를 입력하세요:"))
stack = [None for _ in range(size)]
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
