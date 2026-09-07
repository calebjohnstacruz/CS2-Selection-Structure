#SELECTION STRUCTURE PRACTICE EXERCISES
##Description
  Consists of Problems 1-4

#1.Even or Odd
number = float(input("Please enter a number: "))

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#2.Password Gatekeeper
print("")

word = input("Please enter password: ")

if len(word) >=8:
  print("Password if sufficient")
else:
  print("Too short, I need 8 or more characters!!")

#3.Movie ticket price
print("") 

age = int(input("Please enter your age: "))

if age <= 12:
  print("Ticker price is P180")
elif age >= 13 and age <=64:
  print("Ticket price is P250")
else:
  print("Ticket price is P200")

#4.Leap Year Checker
print("") 

year = int(input("Please enter a year "))

if year % 400 and year % 4 == 0:
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")
