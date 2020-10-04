def check(x,y):
    if x <=0 or y<=0:
        print('오류:0이나 음수를 입력')
        return 4
    else:
        return 0

def gcd(a,b):
    if a<b:
        a,b=b,a
    temp=a%b

    while temp >0:
        a = b
        b = temp
        temp = a%b
    return b

print('분수를 입력하는 코드')
while (True):
    print('숫자 입력 형태 *,*')
    
    A,B = map(int,input('분수1의 두수를 입력해주세요: ').split(','))
    if (check(A,B) == 4):
        continue

    C,D = map(int,input('분수2의 두수를 입력해주세요: ').split(','))
    if (check(C,D) == 4):
        continue

    G = gcd(A*D + C*B, B*D)
    E,F = (A*D + C*B)//G, B*D//G

    print('{}/{} + {}/{} = {}/{}'.format(A,B,C,D,E,F))

    break
