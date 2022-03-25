"""Task : Let's say; you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
Write a program that 

Takes the first name from the user and compares it to yours,
Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later.""""

# Solution

pass_dic = {"Arif" : "ak4563$"}
name = str(input("Please enter your first name :" ))

if name.capitalize() in pass_dic :
    name = name.capitalize()  # ilk harfin kullanıcı tarafından küçük girilme ihtimaline karşı kullandım.
    print("Hello {}! The password is : {}".format(name, pass_dic[name]))
else :
    print("Hello Amina! See you later.")
