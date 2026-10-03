import math

def paint_calc(height, width, coverage):
    number_of_cans = (height * width) / coverage
    round_up_cans = math.ceil(number_of_cans)
    print(f"You will need {round_up_cans} cans of paint.")


height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))
coverage = int(input("Enter coverage (1 can of paint can cover 5 square meters of wall): "))

paint_calc(height, width, coverage)
 