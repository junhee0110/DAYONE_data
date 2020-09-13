'''
1. 두개의 숫자열 (x1,y1), (x2, y2)를 입력받아 x/y 꼴의 분수로 변환하고, 해당 분수 끼리의 합을 출력하는 코드를 작성해보자.

단, 결과값은 기약분수의 형식으로 나타내어야 한다.

출력 예제:
문자열 1 : 1, 5
문자열 2 : 2, 3

1/5 + 2/3 = 13/15
'''

def reduction(top, bottom):
    factor_top = []
    common_factor = []
    for x in range(1,top+1):
        if top%x == 0:
            factor_top.append(x)
    for x in factor_top:
        if bottom%x == 0:
            common_factor.append(x)
    
    max_common = max(common_factor)

    return top//max_common, bottom//max_common


x1, x2 =  input("분수 1을 입력하시오").split('/')
x1 = int(x1)
x2 = int(x2)

x3, x4 =  input("분수 2을 입력하시오").split('/')
x3 = int(x3)
x4 = int(x4)

top = x1*x4 + x2*x3
bottom = x2*x4
top, bottom = reduction(top, bottom)

print("{}/{} + {}/{}".format(x1,x2,x3,x4))
if bottom == 1:
    print(" = {}".format(top))
else:
    print(" = {}/{}".format(top, bottom))