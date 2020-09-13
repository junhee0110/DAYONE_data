x1, y1 = input('문자열 1 : ').split(',')
x2, y2 = input('문자열 2 : ').split(',')
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

a = (x1*y2)+(x2*y1)
b = y1*y2

a = int(a)
b = int(b)

def gcd(a,b) :
    if a < b :
        (a, b) = (b, a)

    while b != 0 :
        (a,b) = (b, a%b)
    return a

ggcd = gcd(a,b)

if ggcd > 1 :
    a = a/ggcd
    b = b/ggcd

a = int(a)
b = int(b)

print(a,'/',b)





