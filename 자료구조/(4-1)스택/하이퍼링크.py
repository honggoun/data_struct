import webbrowser
import time

def isStackFull():
    global size, stack, top
    if(top >= size - 1):
        return True
    else:
        return False

def push(data):
    global size, stack, top
    if(isStackFull()):
        print("스택이 다 찼습니다")
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global size, stack, top
    if(top == -1):
        return True
    else:
        return False
    
def pop():
    global size, stack, top
    if(isStackEmpty()):
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global size, stack, top
    if(isStackEmpty()):
        print("스택이 비어있습니다")
        return None
    return stack[top]

# Initialize stack
size = 100
stack = [None for i in range(size)]
top = -1

# List of URLs (with correct prefixes)
urls = ['https://naver.com', 'https://daum.net', 'https://nate.com']

# Push URLs onto the stack and open them in browser
for url in urls:
    push(url)
    webbrowser.open(url)
    print(url, end='-->')
    time.sleep(1)

print("\n방문종료")
time.sleep(5)

# Pop URLs and revisit them in reverse order
while True:
    url = pop()
    if url is None:
        break
    webbrowser.open(url)
    print(url, end="-->")
    time.sleep(1)

print("\n방문종료")
