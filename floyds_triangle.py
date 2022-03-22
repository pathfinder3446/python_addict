"""Write a function for Floyd's triangle of n rows in Python, you need to ask from user to enter the number of rows or lines up to which.
Sample run of program, with user input 10 as number of rows, is shown in the snapshot given below:"""

row_num = int(input("please enter the number of rows : "))
count = 1
for i in range(1, row_num+1):
    for j in range(1, i+1):
        print(str(count).ljust(2), end=" ")
        count += 1
    print()
