katok = []

def add_Data(data):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = data

def insert_Data(position,insertdata):
    
    if position < 0 or position > len(katok):
        print("데이터 삽입 범위를 벗어났습니다")
        return
    
    katok.append(None)
    klen = len(katok)

    for i in range(klen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None

        katok[i] = insertdata

def delete_Data(position):
    if position < 0 or position > len(katok):
        print("데이터 삽입 범위를 벗어났습니다")
        return
    
    klen = len(katok)
    for i in range(position+1,klen,1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])

if __name__ == "__main__":
    select = -1
    while(select != 4):
        select = int(input("선택하세요(1:추가, 2:삽입, 3:삭제, 4:프로그램 종료)"))
        if select == 1:
            data = input("추가할 데이터를 입력하세요-->")
            add_Data(data)
            print(katok)
        if select == 2:
            position = int(input("삽입할 위치를 입력하세요-->"))
            data = input("삽입할 데이터를 입력하세요-->")
            insert_Data(position,data)
            print(katok)
        if select == 3:
            position = int(input("삭제할 위치를 입력하세요-->"))
            delete_Data(position)
            print(katok)
        if select == 4:
            print("프로그램을 종료합니다")
            exit
        else:
            print("1~4번을 선택하세요")
            continue