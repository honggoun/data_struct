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