"""Write a pyhton code, which is a number guessing game that tries to find the number that will be randomly selected from the number sequence from 1 to 100. and indicate in the code that each user has the right to guess 5, deduct 1 right for each wrong guess"""


from random import randint
numb = randint(1,100)
count = 5
while count > 0:
    guess = int(input("Let's guess the correct number: "))
    print("Enter a number : ", guess)
    if guess > numb:
        print(guess, " decrease the number")
        count -= 1
    elif guess < numb:
        print("increase the number")
        count -= 1
    else:
        print("Congrats !! you guess the correct number")
if count == 0:
    print("your guessing right is over")

