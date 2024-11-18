def isStackFull():
    global SIZE, stack, top
    if(top >= SIZE - 1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print("스택이 다 찼습니다")
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if(isStackEmpty()):
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return None
    return stack[top]

def checkBracket(expr):
    for ch in expr:
        if ch in "([{<":
            push(ch)
        elif ch in ")]}>":
            out = pop()
            if out is None:  # 스택이 비었으면 잘못된 괄호
                return False
            elif ch == ')' and out != '(':
                return False
            elif ch == ']' and out != '[':
                return False
            elif ch == '}' and out != '{':
                return False
            elif ch == '>' and out != '<':
                return False
        else:
            pass
    if isStackEmpty():
        return True
    else:
        return False

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__":

    exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(A+{B-C}/[C*D])>']

    for expr in exprAry:
        top = -1  # 각 식에 대해 스택을 초기화
        print(expr, '==>', checkBracket(expr))
