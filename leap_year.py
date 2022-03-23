"""Find out if a given year is a "leap" year.

  - In the Gregorian calendar, three criteria must be taken into account to identify leap years:
  
    - The year must be evenly divisible by 4;
    - If the year can also be evenly divided by 100, it is not a leap year; unless...(next one)
    - The year is also evenly divisible by 400. Then it is a leap year.

- According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.

- Write a Python program that;
  - Takes a 4-digit year from the user,
  - Prints `True` if the given year by the user is a leap year, prints `False` otherwise."""


# Solution-1

year = int(input("Bir yıl giriniz: "))
result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0)
print("Result is ", result, "\b. The year {} is a leap year if the result is True, otherwise It's not a leap year".format(year)) 


# Solution-2

def is_leap(year):
    
    if 1900<=year and year<=100000:
        leap = False
        if year%4==0 and year%100!=0:
            return True
        
        elif year%400==0 and year%100==0 :
            return True
        
        else:
            return leap
year = int(input())
print(is_leap(year))
