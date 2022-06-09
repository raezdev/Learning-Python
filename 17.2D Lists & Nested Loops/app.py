my_list = [1, 2, 3, 4]
print(my_list)

my_2dList = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(my_2dList)
print(my_2dList[0][0])
print(my_2dList[1][0])
print(my_2dList[2][0])

for lists in my_2dList:
    for row in lists:
        print(row)
