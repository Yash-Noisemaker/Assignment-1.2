n = int(input("Enter a positive integer (n)"))

if n <= 0:
    print("Please enter a positive number")
else:
    sum_n = n*(n+1)//2
    print(f"The sum of first {n} positive integer is: {sum_n}")