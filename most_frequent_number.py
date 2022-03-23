"""After finishing the task correctly, then submit your answer (code) as plain text which shows you did correctly.
Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :
Example
Given list
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
Desired Output
the most frequent number is 3 and it was 4 times repeated"""

# Solution

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

frequent_num = max(numbers, key=numbers.count)
repeat = numbers.count(frequent_num)

print(frequent_num)
print(repeat)

result = f"the most frequent number is {frequent_num} and it was {repeat} \
times repeated"

print(result)
