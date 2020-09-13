'''
2 .10진수를 입력받아 2진수로 변환하여 출력하는 코드를 작성하시오.

출력 예제 :
정수를 입력하세요 : 35
35는 2진법으로 100011
'''

def toBinary(num):
    k = 0
    result = ''
    while True:
        if 2**k > num:
            break
        k += 1
    for x in range(k-1,-1,-1):
        if num - 2**x >= 0:
            result = result + '1'
            num = num - 2**x
        else:
            result = result + '0'
    
    return result

num = int(input("변환할 10진수 입력 : "))
print('{}는 2진수로'.format(num) , toBinary(num))