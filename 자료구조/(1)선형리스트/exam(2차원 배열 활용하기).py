def printpoly(poly):  # 프린트 하는 함수
    polystr = "P(x)="

    for term in poly:
        coef = term[0]  # 계수
        power = term[1]  # 차수

        if coef >= 0:
            polystr += '+'
        polystr += str(coef) + "X^" + str(power) + " "

    return polystr


def calcpoly(xval, poly):  # 값을 계산하는 함수
    retvalue = 0

    for term in poly:
        coef = term[0]  # 계수
        power = term[1]  # 차수
        retvalue += coef * xval ** power
    return retvalue


## 전역 변수 선언 ##
poly = [[7, 300], [-4, 20], [5, 0]]  # 계수와 차수를 2차원 리스트로 저장

## 메인 함수 ##
if __name__ == "__main__":

    pstr = printpoly(poly)
    print(pstr)

    xvalue = int(input("X 값-->"))

    pxvalue = calcpoly(xvalue, poly)
    print(pxvalue)
