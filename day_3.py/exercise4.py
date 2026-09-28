# You've gotten a job at pyhton pizza. Build an automatic pizza order program

print("***** Thank You For Choosing Python Pizza Deliveries! *****")
print(" ")

size = input("What size pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want peperroni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == 'S':
    bill = 15
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        bill += 3
        print(f"Your final bill is ${bill}")
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        bill += 2
        print(f"Your final bill is ${bill}")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

if size == 'M':
    bill = 20
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        bill += 4
        print(f"Your final bill is ${bill}")
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        bill += 3
        print(f"Your final bill is ${bill}")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

if size == 'L':
    bill = 25
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        bill += 4
        print(f"Your final bill is ${bill}")
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        bill += 3
        print(f"Your final bill is ${bill}")
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")