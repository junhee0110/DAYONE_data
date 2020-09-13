'''
3. 2진수 문자열을 입력받아 10진수 정수형으로 반환하는 코드를 작성하시오.
출력 예제:
2진수 숫자를 입력하시오: 100011
100011는 10진수로 35

*각 변환에 대한 함수를 작성하시오
'''

def toDigit(binary):
    result = 0
    binary = list(binary)
    binary.reverse()
    for x in range(len(binary)):
        result += int(binary[x])*(2**x)

    return result

binary = input("변환할 2진수 숫자 입력: ")
print(binary+"는 10진수로",toDigit(binary))
        
