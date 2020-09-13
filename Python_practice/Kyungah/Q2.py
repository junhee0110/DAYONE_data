i=input("정수를 입력하세요 : ")
n=int(i)
a=[]

while(n!=0) :
    div=n//2
    a.append(n%2)
    n=div

a.reverse()
a = ''.join(map(str, a))
print(i,"은 2진법으로",a)


