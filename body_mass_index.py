# Write a program that calculates body mass index from **height** and **weight** entered by the user. 
# Body mass index :  Weight / Height(m) * Height(m)

# Solution


weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))
body_index = weight/height**2
print("Your body mass index: ", body_index)
