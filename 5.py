a = eval(input("Enter the weight(kg): "))
b = eval(input("Enter the height(m): "))

bmi = (a / b**2)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print('Your catogary: Underweight')
if 18.5 <= bmi < 25:
    print('Your catogary: Normal weight')
if 25 <= bmi < 30:
    print('Your catogary: Overweight')
if 30 <= bmi < 39.9:
    print('Your catogary: Obese')
if bmi >= 40.0:
    print('Your catogary: Morbidly obses')