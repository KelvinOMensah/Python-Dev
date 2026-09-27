# Exercise 1
# Write a program that adds the digits in a 2 digit number. 

num = input("Enter a two-digit number: ")

first_digit = int(num[0])
second_digit = int(num[1])

print(first_digit + second_digit)

# Exercise 2
# Write a program that calculates the Body Mass Index(BMI) from a user's weight and height.

weight = int(input("Input your weight(kg): "))
height = float(input("Input your height(m): "))

bmi = weight / height ** 2 

print(int(bmi))

# Exercise 3
# Write a program using maths and f-strings that tells how many weeks left if the user lives until 90 years old. 
# It will take your current age as the input and output a message with time left in this format
# You have x weeks left

age = int(input("Enter your age: "))

years = 90 - age
weeks = years * 52

print(f"You have {weeks} weeks left.")

# PROJECT - TIP CALCULATOR

print("***** Welcome to the tip calculator! *****")
print(" ")

bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give?: 10, 12, or 15(%)?: "))
total_num_of_people = int(input("How many people to split the bill?: "))

final_tip = tip / 100
bill_with_tip = final_tip * bill + bill
bill_per_person = bill_with_tip / total_num_of_people 
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount}")