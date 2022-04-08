"""Given a list such [1,2,3] get an all possible output combinations"""

# SOLUTION-1

solution = [[]]
num =[1,2,3]
num_set = set(num)
for index in range(len(num)):
    solution = [i +[j] for i in solution for j in num_set.difference(set(i))]
    print(solution)


# SOLUTION-2

num = [1,2,3]
b = [[x, y, z] for x in num for y in num for z in num if len(set([x, y, z])) == len(num)]
print(b)
