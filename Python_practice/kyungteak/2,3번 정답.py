def DtB (i): # 10 -> 2
    x=[]

    while i>0:
        x.append(str(i%2))
        i = i//2
        
    x.reverse()
    x=''.join(x)
    return x
    
    
def BtD (j): # 2-> 10
    
    sum = 0
    l = list(j)
    l.reverse()
    
    for g,h in enumerate(l):
        sum += (2**g)*int(h)
    return sum
    


while (True):
    print('진수 변환 코드입니다.')
    print('메뉴')
    print('1. 10진수를 2진수로 바꾸고 싶어요. \n2. 2진수를 10진수로 바꾸고 싶어요.')
    a = int(input('하고 싶은 기능을 선택해주세요: '))
    
    if a==1:
        b=int(input('정수를 입력하세요: '))
        c=DtB(b)
        print('{}는 2진법으로 {}입니다.'.format(b,c))
        break
    
    elif a==2:
        d=input('2진수 숫자를 입력하세요: ')
        e=BtD(d)
        print('{}는 10진법으로 {}입니다.'.format(d,e))
        break
    
    else:
        print('잘못입력하셨습니다.')
        
