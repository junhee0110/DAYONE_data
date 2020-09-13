ori=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# newList=[]

oriRow=len(ori)
e=[element for array in ori for element in array]

def oriColumn() :
    oriRow=len(ori)
    e=[element for array in ori for element in array]
    c=len(e)//oriRow
    return c

print("행의 갯수 : ",oriRow)
print("열의 갯수 : ",oriColumn())

total=oriRow*oriColumn()

newRow=int(input("새로운 행의 갯수 : "))
newColumn=total//newRow
print("새로운 열의 갯수 : ",newColumn)

# if((total%newRow)==0) :
#     for i in range(newRow):
#         line=[]
#         for j in range(newColumn):
#             line.append(e)
#         newList.append(line)


a=0
b=newRow-1

newList = [e[a:b],e[a+newColumn:b+b]]


print(newList)





