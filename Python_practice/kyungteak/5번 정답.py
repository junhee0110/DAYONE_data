result=0
    

while (True):
    
    a = int(input('숫자를 입력해주세요: '))
    
    if a==0: 
        print('0을 입력: 프로그램을 종료함 ')
        print('결과값: {}'.format(result))
        break
    
    elif a>0:
        if a%2 == 0:
            result *=a
        else:
            result +=a
        
    else:
        a= -a
        
        if a%2 ==0:
            result *=a
        else:
            result +=a
