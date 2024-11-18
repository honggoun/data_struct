def printpoly(t_x,p_x):  #프린트 하는 함수
    polystr = "p(x)="

    for i in range(len(p_x)):
        term = t_x[i]  #항차수
        coef = p_x[i]  #계수

        if coef >= 0:
            polystr += '+'
        polystr += str(coef)+"X^"+str(term)+" "

    return polystr

def calcpoly(xval, t_x, p_x):  #값을 계산하는 함수
    retvalue = 0

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retvalue += coef*xval**term
    return retvalue

##전역변수 선언##
tx = [300,20,0]
px = [7,-4,5]

##메인함수##
if __name__ == "__main__":

    pstr = printpoly(tx,px)
    print(pstr)

    xvalue = int(input("x의 값-->"))

    pxvalue = calcpoly(xvalue,tx,px)
    print(pxvalue)