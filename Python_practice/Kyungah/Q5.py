# 5. 사용자가 0을 입력할 때 까지 수를 입력받아 다음의 규칙대로 계산을 수행하는 프로그램을 작성하시오
# [규칙 1] 입력되는 수가 짝수이면 곱하고, 입력되는 수가 홀수이면 더한다.
# [규칙 2] 입력되는 수가 음수라면 절대값으로 [규칙 1]과 같이 연산한다.
#
# EX)5+3 = 8 -> 8×8 = 64 -> 64+23 = 87 -> 87×12 = 1044

i=2
a=0
b=[]


while i!=0 :
    i=int(input())
    b.append(i)

b.pop()
print(b)

l=len(b)-1

def q5() :
    while a<=l :
        value=b[0]
        order=a+1
        orderValue=b[order]
        r=orderValue%2
        if orderValue>0 and r==0 :
            value=value*orderValue
        else:
            if orderValue>0 and r!=0 :
                value=value+orderValue
        return value



qq5 = q5()
print(qq5)










