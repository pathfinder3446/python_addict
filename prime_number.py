Write a program that takes a number from the user and prints the result to check if it is a prime number.

# first solution
n = int(input("Enter a number to check if it is a prime num: "))

counter = 0

for i in range(1, n+1):
    if n % i == 0 :
        counter += 1

if (n == 0) or (n == 1) or (counter >= 3) :
    print(n, " is not a prime number")
else:
    print(n, " is a prime number")


# second solution

inp1 = int(input("Write a number and see if it is prime number or not: "))
flag = True
for i in range(2,inp1):
    if inp1 % i == 0:
        flag = False
        break
    
if flag and inp1 > 1:
    print(f"Yeeah!! {inp1} is prime..")
else:
    print(f"Sorry..{inp1} is not a prime number")


# List of prime numbers

	
limit = int(input("Enter a number bigger than 1: "))
prime_list = []

for i in range(2,limit):
    flag = True
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break

    if flag:
        prime_list.append(i)
print(prime_list)
