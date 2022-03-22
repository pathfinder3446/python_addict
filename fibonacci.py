"""Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function."""

# solution-1

fib_list = [0,1]

for i in range(2,55):
    next_num = fib_list[-1] + fib_list[-2]
    fib_list.append(next_num)
    if fib_list[-1] == 55:
        break

fib_list.pop(0)
print(fib_list)

# solution-2

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
