a = eval(input("Enter the value: "))
b = eval(input("Enter the value: "))

if type(a)==int and type(b)==int:
    result = a + b
    print("Sum:", result)
else:
    print("Both object must be integers!")