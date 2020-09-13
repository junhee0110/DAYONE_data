def form(a,b,c,d):
    num=a*d+b*c
    den=b*d
    mod = num%den
    while mod > 0:
        num = den
        den = mod
        mod = num%den
    print(int((a*d+b*c)/den),"/",int(b*d/den))

    
a,b=map(int, input("문자열 1 : ").split(","))
c,d=map(int, input("문자열 2 : ").split(","))


form(a,b,c,d) 
