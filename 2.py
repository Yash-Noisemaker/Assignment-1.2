num1 = int(input("Enter a value: "))
num2 = int(input("Enter a value: "))

smaller = num1 if num1 < num2 else num2
hcf = 1

for i in range(1, smaller+1):
    if ( num1 % i == 0 ) and ( num2 % i == 0):
        hcf = i
print(f"HCF of {num1} and {num2} is {hcf}")



















# dividend = int(input("Enter a value: "))
# divisor = int(input("Enter a value: "))

# while divisor>1:
#     rem = dividend % divisor
#     if rem == 0:
#         print("HCF:",divisor)
#         break
#     else:
#         dividend = divisor
#         divisor = rem
