def bitode(a):
        dlist=[]
        j=1
        while a!=0:
            if a%10==1:
                dlist.append(j)
                j*=2
                a=a//10
            else:
                    j*=2
                    a=a//10
        j=1
        return sum(dlist)
    
while True:
    a=int(input("10진수로 바꾸고 싶은 2진수를 입력하세요"))
    print(bitode(a))
    

