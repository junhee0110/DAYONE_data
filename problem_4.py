'''
4. n * m 크기의 List와 행의 크기 a를 입력받아 list를 a * x의 List로 재배열하는 함수를 작성하시오.
(빈 공간에는 0을 채워넣는다.)

EX) [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]  ---[ a= 2 ]---> [ [1, 2, 3, 4, 5] , [6, 7, 8, 9, 0] ]
'''

def transForm(array, a):
    one_dim = []
    result = []
    for x in array:
        for y in x:
            one_dim.append(y)
    elem =len(one_dim)
    columns = elem//a
    if elem%a != 0:
        columns += 1
    
    for x in range(a):
        temp = []
        for y in range(columns):
            if x*columns+y+1 <= elem:
                temp.append(one_dim[x*columns+y])
            else:
                temp.append(0)
        result.append(temp)

    return result

def make_array():
    n = int(input("행의 크기를 입력하세요 : "))
    m = int(input("열의 크기를 입력하세요 : "))
    result = []
    for x in range(n):
        temp = []
        for y in range(m):
            temp.append(int(input("{}행 {}열의 값을 입력하세요 : ".format(x+1,y+1))))
        result.append(temp)
    return result

def display_array(array):
    for x in array:
        for y in x:
            print(y,end=" ")
        print("")

original = make_array()
display_array(original)
transformed = transForm(original, int(input("변경할 행의 크기를 입력하세요 : ")))
display_array(transformed)