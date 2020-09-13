def detobi(a): 
    blist=[]
    k=0
    while k!=1:
        n=a%2
        blist.append(n)
        k=a//2
        a=k
        if k==1:
            blist.append(k)
    blist.reverse()
    return("".join(map(str, blist)))
while True:
     a=int(input("2진수로 바꾸고 싶은 10진수를 입력하세요"))
     print(detobi(a))
