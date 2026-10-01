# FizzBuzz game
# Print each number from 1 to 100 in turn and include 100
# When the number is divisible by 3 print "Fizz"
# When the number is divisible by 5 print "Buzz"
# When the number is divisible by 3 and 5 print "FizzBuzz"

print("********** Welcome to the FizzBuzz Game **********")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)