i=input("2진수 숫자를 입력하시오 : ")
a=list(map(int,i))

b=[]

l=len(a)
p=l
o=-1

if(a[-1]==1 or a[-1]==0) :
    for num in a:
        o=o+1
        p=p-1
        q=a[o]*(2**p)
        b.append(q)

d=sum(b)
print(i,"는 10진수로",d)




