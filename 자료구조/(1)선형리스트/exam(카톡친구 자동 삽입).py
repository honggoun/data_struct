##함수 선언##
def add_Data(frind,data):
    katok.append(None)
    klen = len(katok)
    katok[klen -1] = (frind,data)

def insert_Data(frind,data):

    
    katok.append(None)
    klen = len(katok)

    for i in range(klen-1,0,-1):
        if data > katok[i-1][1]:
            katok[i] = katok[i - 1]
        else:
            katok[i] = (frind, data)  # 적절한 위치에 새로운 데이터 삽입
            return

katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
insert_Data('미나', 40)
print(katok)