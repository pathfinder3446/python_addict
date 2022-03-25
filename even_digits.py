"""Question 2:

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

The numbers obtained should be printed in a comma-separated sequence on a single line.
### Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

(Ino order to practice, it's better if you use <b> lambda </b> in your code)"""


# Solution

values = []
for i in range(1000, 3001):
    #s = str(i)
    s = (lambda i: str(i))(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
