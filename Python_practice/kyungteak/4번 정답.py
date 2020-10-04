def rearrlist (c,d):
    a = []
    b = []
    
    for s in c:
        a += s
    
    e= int(len(a)//d) #열계산


    if len(a)%d == 0:
        for n in range(0,len(a),e):
            b.append(a[n:n+e])

    
    
    else:
        e= e+1
    
        w=e*d-len(a)
    
        for m in range(0,w):
            a.append(0)
    
        for o in range(0,len(a),e):
            b.append(a[o:o+e])

    return b
    
while (True):
    
    print('리스트 재배열하는 코드')

    n = int(input('리스트의 행을 입력해주세요: '))
    m = int(input('리스트의 열을 입력해주세요: '))

    x = []

    print('이중리스트에 값을 넣어 주세요')
    for k in range(0,n):
        y=[]
        for t in range(0,m):
            print('{}행{}열'.format(k+1,t+1))
            y.append(input('값을 입력해주세요: '))
        x.append(y)

    print('리스트값을 확인\n{}'.format(x))


    a = int(input('\n새로운 행을 입력해주세요: '))

    if a > n*m :
        print('전체 리스트값 수보다 행이 더 커서 오류')
        continue

    t=rearrlist(x,a)

    print('리스트를 재배열했습니다. \n{}'.format(t))
    break
