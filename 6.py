num = input("Enter an integer: ")

if num.startswith("-"):
    num = num[1:]

total = 0
for digit in num:
    if digit.isdigit():
        total +=int(digit)
    else:
        print("Invalid input! Please enter a valid integer")
        exit()
print(f"The sum of digit is {total}")