
target = int(input("Enter a number between 0 and  101: "))
sum = 0
for number in range(2, target + 1, 2):
    sum += number
print(sum)