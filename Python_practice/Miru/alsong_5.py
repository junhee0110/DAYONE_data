res=int(input())
a=1
while True:
    a=int(input())
    if (a==0):
        break
    elif(a%2==0):
        res=abs(a)*res
    else:
            res=abs(a)+res
print(res)

          
      
     
